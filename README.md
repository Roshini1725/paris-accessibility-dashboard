# Paris Hotel Accessibility & Seasonality Dashboard

An interactive Power BI dashboard analyzing accessible accommodation in Paris — combining real Airbnb listing data with hotel booking seasonality data to surface insights for disabled travelers, accessible-tourism researchers, and hospitality operators.

## Why this project

Accessible travel is a massively underserved analytics niche. Most hotel/booking dashboards optimize for revenue; this one asks a different question: **where, when, and at what price can a wheelchair user or mobility-impaired traveler actually find a place to stay in Paris — and how does demand shift across the year?**

This project was built to demonstrate:
- End-to-end BI workflow: raw data → cleaning (Power Query) → modeling (DAX) → storytelling (report design)
- Comfort working with real-world, imperfect, multi-source data
- An analytical angle grounded in inclusive design / privacy-and-accessibility-by-design thinking

## Data sources

| Dataset | Source | Used for |
|---|---|---|
| Airbnb Paris Listings | [Kaggle - juliatb/airbnb-paris](https://www.kaggle.com/datasets/juliatb/airbnb-paris) | Accessibility amenities, arrondissement geography, pricing, guest ratings |
| Hotel Booking Demand | [Kaggle - jessemostipak/hotel-booking-demand](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand) | Monthly booking volume / seasonal demand pattern, forecast |

> Note: no single public dataset combines Paris accessibility data with multi-year booking seasonality. This project deliberately combines two real, independently-sourced datasets — a common real-world analytics scenario — and documents that decision transparently rather than presenting it as one native source.

## Dashboard pages

1. **Overview** — KPI summary: total listings, % accessible, avg. price, avg. rating
2. **Accessibility Features** — breakdown of wheelchair access, elevators, step-free entry, accessible bathrooms across listings
3. **Pricing Comparison** — accessible vs. standard room/listing pricing
4. **Geographic Distribution** — accessible listing density by Paris arrondissement (bar/column, no map per scope)
5. **Guest Ratings** — rating patterns for listings tagged with accessibility features
6. **Seasonal Demand & Forecast** — monthly booking volume with Power BI's built-in forecast line

## Tech stack

- **Power BI Desktop** (Power Query for ETL, DAX for measures)
- **Python (pandas)** for pre-cleaning/merging the two raw datasets before import
- **Kaggle** as data source

## Repo structure

```
paris-accessibility-dashboard/
├── README.md
├── CASE_STUDY.md
├── data/
│   ├── raw/                  # place downloaded Kaggle CSVs here
│   └── processed/            # output of data_prep.py, ready for Power BI
├── scripts/
│   └── data_prep.py          # cleans & merges the two datasets
├── powerbi/
│   ├── BUILD_GUIDE.md        # step-by-step instructions to build the .pbix
│   ├── DAX_MEASURES.md       # every DAX measure used, ready to paste
│   └── paris_accessibility_dashboard.pbix   # add after building
└── docs/
    └── screenshots/          # dashboard page screenshots for this README
```

## How to reproduce

1. Download the two datasets from Kaggle (links above) into `data/raw/`
2. Run `python scripts/data_prep.py` to generate clean, merged CSVs in `data/processed/`
3. Open Power BI Desktop → follow `powerbi/BUILD_GUIDE.md` page by page
4. Use `powerbi/DAX_MEASURES.md` for all calculated measures
5. Export screenshots into `docs/screenshots/` and embed them below

## Results preview

*(Add screenshots here once built — see docs/screenshots/)*

## Key insights

See [CASE_STUDY.md](./CASE_STUDY.md) for the full write-up of findings and recommendations.


