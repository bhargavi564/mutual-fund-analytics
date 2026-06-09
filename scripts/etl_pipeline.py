import pandas as pd
import os

DATA_PATH = "data/raw"

csv_files = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

summary = []

for file in csv_files:

    filepath = os.path.join(DATA_PATH, file)

    df = pd.read_csv(filepath)

    print("\n" + "="*50)
    print(f"Dataset: {file}")
    print("="*50)

    print("Shape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nHead:")
    print(df.head())

    missing_values = df.isnull().sum().sum()

    summary.append({
        "Dataset": file,
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": missing_values
    })

summary_df = pd.DataFrame(summary)

summary_df.to_csv(
    "reports/day1_dataset_summary.csv",
    index=False
)

print("\nData ingestion completed successfully.")

duplicates = df.duplicated().sum()

print("Duplicate Rows:" ,duplicates)

print("Missing Values:")

print(df.isnull().sum())

df['launch_date'] = pd.to_datetime(df['launch_date'], errors='coerce')

print(df['launch_date'].isnull().sum())

missing_codes = set(fund_master['amfi_code'])-set(nav_history_codes['amfi_code'])

print(missing_codes)

df[df['nav']>1000]

print("Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


