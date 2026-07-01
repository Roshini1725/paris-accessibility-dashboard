# DAX Measures Reference

Copy-paste these into Power BI: right-click the **Listings** (or **SeasonalDemand**) table in the Fields pane → **New Measure** → paste.

## Listings table measures

```dax
Total Listings = COUNTROWS(Listings)
```

```dax
Accessible Listings = CALCULATE(COUNTROWS(Listings), Listings[is_accessible] = TRUE)
```

```dax
% Accessible Listings = DIVIDE([Accessible Listings], [Total Listings], 0)
```

```dax
Average Price = AVERAGE(Listings[price])
```

```dax
Average Price (Accessible) =
CALCULATE(AVERAGE(Listings[price]), Listings[is_accessible] = TRUE)
```

```dax
Average Price (Standard) =
CALCULATE(AVERAGE(Listings[price]), Listings[is_accessible] = FALSE)
```

```dax
Price Gap (Accessible vs Standard) =
[Average Price (Accessible)] - [Average Price (Standard)]
```

```dax
Average Rating = AVERAGE(Listings[rating])
```

```dax
Average Rating (Accessible) =
CALCULATE(AVERAGE(Listings[rating]), Listings[is_accessible] = TRUE)
```

```dax
Min Price = MIN(Listings[price])
```

```dax
Max Price = MAX(Listings[price])
```

## SeasonalDemand table measures

```dax
Total Bookings = SUM(SeasonalDemand[bookings])
```

```dax
Average Monthly Bookings = AVERAGE(SeasonalDemand[bookings])
```

```dax
Peak Month Bookings = MAX(SeasonalDemand[bookings])
```

> Forecast itself doesn't need a DAX measure — it's added directly on the line chart via the Analytics pane (see BUILD_GUIDE.md step 9).

## Tips for a beginner

- Measures auto-calculate based on filter context — the same `[Average Price]` measure will recalculate correctly whether you're looking at all listings, one arrondissement, or one accessibility flag, with zero extra formulas needed.
- Use `DIVIDE()` instead of `/` in DAX — it safely handles divide-by-zero (returns the third argument, here `0`, instead of erroring).
- Format each measure (e.g. as currency or percentage) via the **Measure Tools** ribbon after creating it, not inside the DAX formula itself.
