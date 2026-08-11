SELECT
    contract_type,
    internet_service,
    COUNT(*) FILTER (WHERE churned = 1)                     AS churned_customers,
    ROUND(SUM(monthly_charges) FILTER (WHERE churned = 1), 2) AS monthly_revenue_at_risk,
    ROUND(AVG(tenure_months) FILTER (WHERE churned = 1), 1)   AS avg_tenure_before_churn
FROM {{ ref('stg_customers') }}
GROUP BY contract_type, internet_service
ORDER BY monthly_revenue_at_risk DESC
