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

-- 1 Top 5 Funds by AUM
SELECT *
FROM fact_aum
ORDER BY aum DESC
LIMIT 5;

-- 2 Average NAV
SELECT amfi_code,
AVG(nav)
FROM fact_nav
GROUP BY amfi_code;

-- 3 SIP Growth
SELECT *
FROM fact_transactions
WHERE transaction_type='SIP';

-- 4 Transactions by State
SELECT state,
COUNT(*)
FROM fact_transactions
GROUP BY state;

-- 5 Expense Ratio <1%
SELECT *
FROM fact_performance
WHERE expense_ratio <1;

-- 6 Total Funds
SELECT COUNT(*)
FROM dim_fund;

-- 7 Average Return
SELECT AVG(return_1yr)
FROM fact_performance;

-- 8 Highest NAV
SELECT MAX(nav)
FROM fact_nav;

-- 9 Total AUM
SELECT SUM(aum)
FROM fact_aum;

-- 10 Fund Count by Category
SELECT category,
COUNT(*)
FROM dim_fund
GROUP BY category;