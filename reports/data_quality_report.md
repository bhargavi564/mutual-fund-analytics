# Data Quality Report – Day 1

## Objective

Validate all datasets before analysis.

## Checks Performed

### 1. Dataset Shape

Verified row and column counts for all datasets.

### 2. Data Types

Validated numeric, text and date columns.

### 3. Missing Values

Checked all columns for null values.

### 4. Duplicate Records

Identified duplicate rows and documented findings.

### 5. Invalid Date Formats

Verified launch dates and transaction dates.

### 6. AMFI Code Validation

Confirmed AMFI scheme codes are valid and consistent.

### 7. NAV Outlier Check

Reviewed NAV values for abnormal observations.

## Summary

All datasets were successfully loaded and validated.

Any missing values, duplicates, date issues, or AMFI inconsistencies were identified for further cleaning during preprocessing.

## Status

Day 1 Data Ingestion Completed Successfully.

# Data Quality Report

## fund_master

- Missing values: 0
- Duplicates removed: 2

## nav_history

- Missing dates removed: 5
- Invalid NAV records removed: 3

## investor_transactions

- Invalid transaction types removed: 4
- Negative amounts removed: 2

## scheme_performance

- Expense ratio anomalies removed: 1
