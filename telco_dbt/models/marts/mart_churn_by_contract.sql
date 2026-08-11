SELECT
    contract_type,
    COUNT(*)                                    AS total_customers,
    SUM(churned)                                AS churned_customers,
    ROUND(AVG(churned) * 100, 1)               AS churn_rate_pct,
    ROUND(AVG(monthly_charges), 2)             AS avg_monthly_charges
FROM {{ ref('stg_customers') }}
GROUP BY contract_type
ORDER BY churn_rate_pct DESC
