# Case Study: Paris Hotel Accessibility & Seasonality Dashboard

## Problem

Accessible travel planning is hard. Disabled travelers searching for accommodation in Paris have no easy way to compare accessibility features, pricing fairness, and availability patterns across the city. Most travel BI projects optimize purely for revenue or occupancy and ignore accessibility as an analytical dimension entirely. This project treats accessibility as a first-class metric, not a footnote.

## Approach

1. **Data sourcing**: Combined two real, independently published Kaggle datasets — Airbnb Paris listings (for accessibility amenities, location, price, ratings) and Hotel Booking Demand (for monthly booking seasonality) — since no single source covers both dimensions for Paris.
2. **Cleaning**: Used Python/pandas to standardize amenity tags into a consistent "accessibility flag" taxonomy (wheelchair accessible, step-free access, elevator, accessible bathroom), handle missing values, and align date fields for the seasonality merge.
3. **Modeling**: Built a star-schema-style model in Power BI with a fact table of listings/bookings and supporting dimension tables (arrondissement, accessibility feature, month).
4. **Visualization**: Designed 6 report pages moving from a high-level KPI overview down to specific accessibility, pricing, geographic, ratings, and seasonal-forecast views.

## Key insights

*(Fill in with your actual numbers once the dashboard is built — placeholders below show the expected shape of findings)*

- Only a minority of Paris listings explicitly tag accessibility features, suggesting a supply gap or a data/labeling gap (worth noting which).
- Accessible listings show [higher/lower/comparable] average pricing versus standard listings — relevant for fairness discussions.
- Accessibility-tagged listings cluster in [X] arrondissements, often correlating with proximity to major transit/tourist hubs — or revealing underserved areas.
- Guest ratings for accessibility-tagged listings are [comparable to / higher than / lower than] the citywide average, suggesting [satisfaction / room for improvement].
- Booking demand peaks in [month(s)], with Power BI's built-in forecast projecting continued seasonal growth into the next cycle — useful for accessible-accommodation operators planning capacity.

## Recommendations

- Platforms like Airbnb/booking sites should standardize and surface accessibility tags more consistently — inconsistent labeling is itself a finding worth highlighting.
- Hosts/hotels in underserved arrondissements could be flagged as opportunities for accessible-accommodation investment.
- Pricing parity (or the lack of it) between accessible and standard listings is worth surfacing publicly, as it touches both customer fairness and inclusive design ethics.

## Limitations

- Two datasets from different sources/time periods were combined; seasonality patterns come from a general European hotel dataset, not Paris-specific bookings, so the forecast page should be read as illustrative of *general* seasonal hospitality demand rather than a precise Paris accessible-stay forecast.
- Accessibility tagging in the source data reflects self-reported host/platform fields, not independently verified accessibility audits.

## Skills demonstrated

Power Query (ETL), DAX (measures, time intelligence, forecasting), data modeling, Python/pandas for pre-processing, dashboard/report design, and an accessibility-and-ethics-aware analytical framing consistent with a privacy/inclusive-design-by-design approach to data work.
