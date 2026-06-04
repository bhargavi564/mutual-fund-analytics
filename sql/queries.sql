-- Total number of schemes

SELECT COUNT(*) AS total_schemes
FROM fund_master;

-- Equity funds

SELECT *
FROM fund_master
WHERE category='Equity';

-- Large Cap Funds

SELECT *
FROM fund_master
WHERE sub_category='Large Cap';

-- Average Expense Ratio

SELECT AVG(expense_ratio_pct)
FROM fund_master;