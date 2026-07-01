# Power BI Build Guide

Follow this top to bottom in Power BI Desktop (free download from Microsoft — no Microsoft 365 subscription needed). Total time: ~60–90 minutes as a beginner.

## 1. Import data

1. Open Power BI Desktop → **Get Data → Text/CSV**
2. Import `data/processed/listings_clean.csv` → name it **Listings**
3. Repeat: import `data/processed/seasonal_demand.csv` → name it **SeasonalDemand**
4. Click **Transform Data** to open Power Query Editor

## 2. Clean in Power Query

**Listings table:**
- Confirm `price` is type **Decimal Number**
- Confirm `rating` is type **Decimal Number**
- Confirm `is_accessible` is type **True/False**
- Rename `neighbourhood` → `Arrondissement` (Right-click column → Rename)

**SeasonalDemand table:**
- Confirm `bookings` is **Whole Number**
- Confirm `month` is **Text**, `year` is **Whole Number**
- Add a Custom Column `MonthYear` = `Text.From([month]) & " " & Text.From([year])` for chronological sorting later

Click **Close & Apply**.

## 3. Build the data model

1. Go to the **Model** view (left sidebar)
2. These two tables are independent (no shared key) — that's fine, they power separate report pages
3. Optional: create a simple **Calendar** table via *New Table*:
   ```
   Calendar = CALENDAR(DATE(2024,1,1), DATE(2025,12,31))
   ```

## 4. Page 1 — Overview

Add Card visuals (Insert → Card) for each KPI measure from `DAX_MEASURES.md`:
- Total Listings
- % Accessible Listings
- Average Price
- Average Rating

Add a Donut chart: `is_accessible` (legend) by count of listings.

## 5. Page 2 — Accessibility Features

1. Add a new column in Power Query or DAX to split `amenities_raw` into individual tags (or use the pre-flagged `is_accessible` boolean for simplicity as a beginner)
2. Bar chart: count of listings by `is_accessible` (Yes/No)
3. Table visual: list of accessibility-flagged listings with neighbourhood, price, rating

## 6. Page 3 — Pricing Comparison

1. Clustered column chart: Average Price by `is_accessible` (Yes/No)
2. Box-and-whisker style isn't native — use a clustered bar of Min/Avg/Max price by accessibility flag instead (3 measures, same chart)

## 7. Page 4 — Geographic Distribution

1. Bar chart: count of `is_accessible = True` listings by `Arrondissement`
2. Sort descending so the most accessible-friendly areas are obvious at a glance

## 8. Page 5 — Guest Ratings

1. Clustered column: Average Rating by `is_accessible`
2. Scatter chart: Price (x-axis) vs Rating (y-axis), colored by `is_accessible` — reveals if accessible listings are priced fairly relative to quality

## 9. Page 6 — Seasonal Demand & Forecast

1. Switch to the **SeasonalDemand** table
2. Line chart: `bookings` (y-axis) by `MonthYear` (x-axis), sorted chronologically (right-click axis → Sort by → use a numeric Month index column if order looks wrong)
3. Click on the chart → open the **Analytics** pane (magnifying-glass icon) → **Forecast** → click **Add** → set forecast length (e.g. 6 periods) → **Apply**
4. This adds a dotted forecast line + confidence interval automatically — no DAX or coding needed

## 10. Apply the theme

Go to **View → Themes → Browse for themes** and import a custom theme JSON, or manually set:
- Primary: soft teal `#4A9B9B`
- Accent: warm coral `#E8845C`
- Background: off-white `#FAFAF7`
- Text: charcoal `#2D2D2D`

This calm, accessible palette (not garish, good contrast) fits the inclusive-design theme better than a generic corporate blue.

## 11. Final touches

- Add a text box title on each page
- Add a Page Navigator (Insert → Buttons → Navigator) for easy click-through
- File → Export → Export to PDF (handy for sharing alongside the .pbix)
- Save as `paris_accessibility_dashboard.pbix` in the `powerbi/` folder
- Take a screenshot of each page → save into `docs/screenshots/` → embed in README

## 12. Publish to GitHub

Power BI files are binary — GitHub will store them fine but won't render previews. That's exactly why the README screenshots + this build guide matter: they let viewers "see" the dashboard without opening Power BI.
