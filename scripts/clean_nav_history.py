#Clean nav_history.csv

import pandas as pd

df=pd.read_csv('data/raw/nav_history.csv')

df['date'] = pd.to_datetime(df['date'])

df=df.sort_values(['amfi_code','date'])

df['nav']=df.groupby('amfi_code')['nav'].ffill()

df=df.drop_duplicates()

df=df[df['nav']>0]

df.to_csv(
     "data/processed/nav_history_clean.csv",
              index=False         
)

#Clean investor_transactions.csv

import pandas as pd

df = pd.read_csv("data/raw/investor_transactions.csv")

df['transaction_date'] = pd.to_datetime(
    df['transaction_date']
)

df['transaction_type'] = (
    df['transaction_type']
    .str.upper()
)

df = df[
    df['transaction_type']
    .isin(['SIP','LUMPSUM','REDEMPTION'])
]

df = df[df['amount'] > 0]

df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)


#Clean scheme_performance.csv

import pandas as pd

df = pd.read_csv(
    "data/raw/scheme_performance.csv"
)

df['return_1yr'] = pd.to_numeric(
    df['return_1yr'],
    errors='coerce'
)

df = df[
    (df['expense_ratio'] >= 0.1)
    &
    (df['expense_ratio'] <= 2.5)
]

df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)