import pandas as pd
import os

raw_path = "data/raw"
processed_path = "data/processed"

os.makedirs(processed_path, exist_ok=True)

for file in os.listdir(raw_path):

    if file.endswith(".csv"):

        print(f"Cleaning {file}")

        df = pd.read_csv(os.path.join(raw_path, file))

        # Remove duplicates
        df = df.drop_duplicates()

        # Remove extra spaces from column names
        df.columns = df.columns.str.strip()

        # Fill missing values
        df = df.fillna("Unknown")

        # Save cleaned file
        clean_name = file.replace(".csv", "_clean.csv")

        df.to_csv(
            os.path.join(processed_path, clean_name),
            index=False
        )

print("All files cleaned successfully!")


import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

# Remove duplicates
df = df.drop_duplicates()

# Convert date
df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

# Remove invalid dates
df = df.dropna(subset=["date"])

# NAV should be positive
df = df[df["nav"] > 0]

df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("NAV cleaned")

import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.upper()
)

# Keep valid types only
valid = [
    "SIP",
    "LUMPSUM",
    "REDEMPTION"
]

df = df[
    df["transaction_type"].isin(valid)
]

# Amount must be positive
df = df[df["amount"] > 0]

df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Transactions cleaned")




import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

# Convert returns to numeric
for col in ["1yr_return","3yr_return","5yr_return"]:

    if col in df.columns:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

# Remove missing rows
df = df.dropna()

# Expense ratio check
if "expense_ratio" in df.columns:
    df = df[
        (df["expense_ratio"] >= 0.1)
        &
        (df["expense_ratio"] <= 2.5)
    ]

df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("Performance cleaned")




