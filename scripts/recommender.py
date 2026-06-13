import pandas as pd

scorecard = pd.read_csv(
    "data/processed/07_scheme_performance_clean.csv"
)

risk = input(
    "Enter Risk Level (Low/Moderate/High/Very High): "
)

result = scorecard[
    scorecard["risk_category"].str.lower()
    == risk.lower()
]

result = result.sort_values(
    by="sharpe_ratio",
    ascending=False
)

print("\nTop 3 Recommended Funds\n")

print(
    result[
        [
            "scheme_name",
            "fund_house",
            "sharpe_ratio",
            "return_3y",
            "risk_category"
        ]
    ].head(3)
)