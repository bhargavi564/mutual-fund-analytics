import pandas as pd

scorecard = pd.read_csv(
    "../data/processed/07_scheme_performance_clean.csv"
)

print("\n========== COLUMNS ==========")
for col in scorecard.columns:
    print(col)

print("\n========== SAMPLE DATA ==========")
print(scorecard.head())

input("\nPress Enter to exit...")
print(scorecard.columns.tolist())



import pandas as pd

scorecard = pd.read_csv(
    "../data/processed/07_scheme_performance_clean.csv"
)

risk = input(
    "Enter Risk Level (Low/Moderate/High/Very High): "
)

result = scorecard[
    scorecard["risk_grade"].str.lower()
    == risk.lower()
]

result = result.sort_values(
    by="sharpe_ratio",
    ascending=False
)

print("\nTop 3 Recommended Funds:\n")

print(
    result[
        [
            "scheme_name",
            "fund_house",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct"
        ]
    ].head(3)
)
