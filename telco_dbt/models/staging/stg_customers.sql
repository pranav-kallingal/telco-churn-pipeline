WITH source AS (
    SELECT * FROM {{ ref('telco_churn') }}
),

cleaned AS (
    SELECT
        customerID                                          AS customer_id,
        gender                                              AS gender,
        CAST(SeniorCitizen AS INT)                         AS is_senior_citizen,
        CASE WHEN Partner = 'Yes' THEN 1 ELSE 0 END        AS has_partner,
        CASE WHEN Dependents = 'Yes' THEN 1 ELSE 0 END     AS has_dependents,
        CAST(tenure AS INT)                                 AS tenure_months,
        PhoneService                                        AS phone_service,
        MultipleLines                                       AS multiple_lines,
        InternetService                                     AS internet_service,
        OnlineSecurity                                      AS online_security,
        Contract                                            AS contract_type,
        PaperlessBilling                                    AS paperless_billing,
        PaymentMethod                                       AS payment_method,
        CAST(MonthlyCharges AS DOUBLE)                      AS monthly_charges,
        CASE 
            WHEN TRIM(TotalCharges) = '' THEN NULL
            ELSE CAST(TRIM(TotalCharges) AS DOUBLE)
        END                                                 AS total_charges,
        CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END          AS churned
    FROM source
)

SELECT * FROM cleaned
