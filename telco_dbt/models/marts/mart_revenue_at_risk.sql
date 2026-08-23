SELECT
contract_type,
internet_service,
SUM(CASE WHEN churned = 1 THEN 1 ELSE 0 END)                           AS churned_customers,
ROUND(SUM(CASE WHEN churned = 1 THEN monthly_charges ELSE 0 END), 2)   AS monthly_revenue_at_risk,
ROUND(AVG(CASE WHEN churned = 1 THEN tenure_months ELSE NULL END), 1) AS avg_tenure_before_churn
FROM {{ ref('stg_customers') }}
GROUP BY contract_type, internet_service
ORDER BY monthly_revenue_at_risk DESC