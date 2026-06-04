CREATE TABLE dim_fund(
    fund_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    scheme_name TEXT,
    category TEXT
);

CREATE TABLE dim_date(
    date_id INTEGER PRIMARY KEY,
    full_date DATE
);

CREATE TABLE fact_nav(
    nav_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    date DATE,
    nav REAL
);

CREATE TABLE fact_transactions(
    transaction_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    amount REAL,
    transaction_type TEXT
);

CREATE TABLE fact_performance(
    performance_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    return_1yr REAL
);

CREATE TABLE fact_aum(
    aum_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    aum REAL
);