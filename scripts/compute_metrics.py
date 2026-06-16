"""
Mutual Fund Analytics Project
Author: Bhargavi Yeramgari
Purpose: Calculate CAGR, Sharp RAtio, Sortino Ratio and other metrics.
"""
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

df = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("Performance metrics calculated Successfully")