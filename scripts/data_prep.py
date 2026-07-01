"""
data_prep.py
Cleans and merges the two source datasets into Power BI-ready CSVs.

BEFORE RUNNING:
1. Download from Kaggle and place in data/raw/:
   - airbnb_paris.csv        (from kaggle.com/datasets/juliatb/airbnb-paris)
   - hotel_booking_demand.csv (from kaggle.com/datasets/jessemostipak/hotel-booking-demand)

NOTE: Kaggle dataset column names can vary slightly between versions/uploads.
This script prints the actual columns it finds and uses flexible matching;
adjust the COLUMN MAPPING section below if a column isn't auto-detected.

Run with: python scripts/data_prep.py
"""

import pandas as pd
import os
import re

RAW_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "processed")
os.makedirs(OUT_DIR, exist_ok=True)

ACCESSIBILITY_KEYWORDS = [
    "wheelchair", "step-free", "step free", "accessible", "elevator",
    "lift", "ramp", "ground floor", "wide doorway", "grab bar", "roll-in"
]


def find_col(df, candidates):
    """Return the first matching column name (case-insensitive, substring match)."""
    cols_lower = {c.lower(): c for c in df.columns}
    for cand in candidates:
        for col_lower, col_orig in cols_lower.items():
            if cand in col_lower:
                return col_orig
    return None


def flag_accessibility(text):
    if not isinstance(text, str):
        return False
    text_lower = text.lower()
    return any(kw in text_lower for kw in ACCESSIBILITY_KEYWORDS)


def process_airbnb():
    path = os.path.join(RAW_DIR, "airbnb_paris.csv")
    if not os.path.exists(path):
        print(f"[skip] {path} not found yet — download it from Kaggle first.")
        return None

    df = pd.read_csv(path, low_memory=False)
    print("Airbnb Paris columns found:", list(df.columns))

    col_amenities = find_col(df, ["amenities"])
    col_price = find_col(df, ["price"])
    col_neighbourhood = find_col(df, ["neighbourhood", "arrondissement", "district"])
    col_rating = find_col(df, ["review_scores_rating", "rating"])
    col_room_type = find_col(df, ["room_type", "property_type"])
    col_id = find_col(df, ["id"])

    keep_cols = {k: v for k, v in {
        "listing_id": col_id,
        "neighbourhood": col_neighbourhood,
        "price": col_price,
        "rating": col_rating,
        "room_type": col_room_type,
        "amenities_raw": col_amenities,
    }.items() if v is not None}

    clean = df[list(keep_cols.values())].copy()
    clean.columns = list(keep_cols.keys())

    # Clean price (strip currency symbols if present)
    if "price" in clean.columns:
        clean["price"] = (
            clean["price"].astype(str)
            .str.replace(r"[^\d.]", "", regex=True)
            .replace("", None)
            .astype(float)
        )

    # Flag accessibility from amenities text
    if "amenities_raw" in clean.columns:
        clean["is_accessible"] = clean["amenities_raw"].apply(flag_accessibility)
    else:
        clean["is_accessible"] = False
        print("[warning] No amenities column found — accessibility flag defaulted to False. "
              "Check the raw CSV columns and update find_col candidates above.")

    clean = clean.dropna(subset=["price"]) if "price" in clean.columns else clean
    out_path = os.path.join(OUT_DIR, "listings_clean.csv")
    clean.to_csv(out_path, index=False)
    print(f"[done] Wrote {len(clean)} rows to {out_path}")
    return clean


def process_hotel_demand():
    path = os.path.join(RAW_DIR, "hotel_booking_demand.csv")
    if not os.path.exists(path):
        print(f"[skip] {path} not found yet — download it from Kaggle first.")
        return None

    df = pd.read_csv(path, low_memory=False)
    print("Hotel Booking Demand columns found:", list(df.columns))

    col_year = find_col(df, ["arrival_date_year"])
    col_month = find_col(df, ["arrival_date_month"])
    col_hotel = find_col(df, ["hotel"])
    col_cancel = find_col(df, ["is_canceled"])

    needed = [c for c in [col_year, col_month, col_hotel, col_cancel] if c]
    clean = df[needed].copy()
    rename_map = {}
    if col_year: rename_map[col_year] = "year"
    if col_month: rename_map[col_month] = "month"
    if col_hotel: rename_map[col_hotel] = "hotel_type"
    if col_cancel: rename_map[col_cancel] = "is_canceled"
    clean = clean.rename(columns=rename_map)

    if "is_canceled" in clean.columns:
        clean = clean[clean["is_canceled"] == 0]

    if "year" in clean.columns and "month" in clean.columns:
        monthly = (
            clean.groupby(["year", "month"])
            .size()
            .reset_index(name="bookings")
        )
        month_order = ["January", "February", "March", "April", "May", "June",
                        "July", "August", "September", "October", "November", "December"]
        monthly["month"] = pd.Categorical(monthly["month"], categories=month_order, ordered=True)
        monthly = monthly.sort_values(["year", "month"])
    else:
        monthly = clean

    out_path = os.path.join(OUT_DIR, "seasonal_demand.csv")
    monthly.to_csv(out_path, index=False)
    print(f"[done] Wrote {len(monthly)} rows to {out_path}")
    return monthly


if __name__ == "__main__":
    print("=== Processing Airbnb Paris listings ===")
    process_airbnb()
    print("\n=== Processing Hotel Booking Demand (seasonality) ===")
    process_hotel_demand()
    print("\nAll done. Check data/processed/ for listings_clean.csv and seasonal_demand.csv")
    print("Import both CSVs into Power BI via Get Data > Text/CSV.")
