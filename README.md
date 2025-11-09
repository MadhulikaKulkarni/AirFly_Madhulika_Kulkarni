# Flights Delay Analysis – Milestone 1

## What I Did

For Milestone 1, I cleaned and prepared the flight dataset to make it ready for analysis.


## Dataset

* Original dataset: `flights_sample_3m.csv`
* Cleaned dataset: `flights_cleaned_for_dashboard.csv `


## Steps I Did

1. Loaded the dataset using pandas.
2. Checked columns, data types, and missing values.
3. Removed or handled null/missing values.
4. Renamed some columns for clarity.
5. Added new columns:

   - `YEAR`
   - `MONTH`
   - `DAY_OF_WEEK`
   - `WEEKEND` (0 = weekday, 1 = weekend)
   - `ROUTE` (Origin-Destination)
   - `CRS_DEP_HOUR` (hour extracted from scheduled departure)
   - `ARR_DELAY_CATEGORY` (On Time / Delayed)
6. Saved the cleaned dataset as `flights_dashboard_final.csv`.

---

## Columns After Cleaning

- FL_DATE, AIRLINE, AIRLINE_DOT, AIRLINE_CODE, DOT_CODE, FL_NUMBER
- ORIGIN, ORIGIN_CITY, DEST, DEST_CITY
- CRS_DEP_TIME, DEP_TIME, DEP_DELAY, TAXI_OUT, WHEELS_OFF, WHEELS_ON, TAXI_IN
- CRS_ARR_TIME, ARR_TIME, ARR_DELAY, CANCELLED, CANCELLATION_CODE, DIVERTED
- CRS_ELAPSED_TIME, ELAPSED_TIME, AIR_TIME, DISTANCE
- DELAY_DUE_CARRIER, DELAY_DUE_WEATHER, DELAY_DUE_NAS, DELAY_DUE_SECURITY, DELAY_DUE_LATE_AIRCRAFT
- YEAR, MONTH, DAY_OF_WEEK, WEEKEND, ROUTE, CRS_DEP_HOUR, ARR_DELAY_CATEGORY


## Tools

- Python
- Pandas
- VS Code


## links

- [Cleaned Dataset (Google Drive)](https://drive.google.com/file/d/1_-ZiULV8Ct50tGpQHzpNg0zPU-CXWBCl/view?usp=sharing)
- [Original Dataset](https://drive.google.com/file/d/12DIgIAQ799sRB0g3XErjMtgo11elXmJG/view?usp=drive_link)

## Status

Milestone 1 is complete. The dataset is now ready for Milestone 2
