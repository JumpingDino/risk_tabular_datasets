# Risk Tabular Datasets

This document contains a curated list of publicly available datasets commonly used for credit risk analysis and modeling. Each dataset provides information about credit applicants and their associated risk factors.

## Sources

| Dataset | 
|---------|
| German Credit Data |
| Taiwan Credit Risk Dataset |

All datasets contain the target variable renamed as `target`. A column named as `_is_test` was created so the user can split the train/validation/calibration sets from the test partition. The split assignment is randomly being 25% for the positive boolean(True) and 75% for the False.

More information about dataset and field description and pre-processing can be seen on the respective dataset section.

Any preprocessing scripts used to improve data readability or for train/test assignment can be found on the `scripts` folder. The final data can be seen on the `data/` folder and the raw dataset before the preprocessing can be seen on the `data/raw` folder.

## Datasets

### German Credit Data
- **Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data)
- **Description**: A widely-used dataset containing attributes and credit risk classifications for 1000 loan applicants. Includes demographic information, credit history, loan details, and other financial characteristics.
- **Link**: https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data

##### Fields
| column_name             | type        | description                                                                                                                                                     |
| ----------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| status_account          | categorical | Checking account status / balance band (qualitative indicator of current account standing, e.g., negative balance, low/medium balance, or no checking account in DM(Deutsche Mark)). |
| month_duration          | numerical   | Loan duration in months (how long the credit is taken for).                                                                                                     |
| credit_history          | categorical | Past credit repayment history category (e.g., no prior credits, paid back duly, delays, or “critical account”).                                                 |
| purpose                 | categorical | Stated purpose of the loan (e.g., car, furniture, education, business, etc.).                                                                                   |
| credit_amount           | numerical   | Loan principal / credit amount requested or granted.                                                                                                            |
| status_savings          | categorical | Savings account / savings balance band (e.g., < 100 DM up to ≥ 1000 DM, or unknown/no savings).                                                                 |
| years_employment        | categorical | Employment status / length of current employment in grouped categories (e.g., unemployed, <1 year, 1–4 years, etc.).                                            |
| payment_to_income_ratio | numerical   | Installment rate as a share of disposable income (a numeric ratio/encoded level representing how heavy the payment burden is relative to income).               |
| status_and_sex          | categorical | Combined marital/relationship status and sex category (encoded demographic grouping used by the dataset).                                                       |
| secondary_obligor       | categorical | Presence/type of additional obligor on the loan (none, co-applicant, or guarantor).                                                                             |
| residence_since         | numerical   | Years at current residence (tenure at the present address).                                                                                                     |
| collateral              | categorical | Type of collateral / assets pledged or available (e.g., none, car, real estate, life insurance/savings agreement).                                              |
| age                     | numerical   | Applicant age in years.                                                                                                                                         |
| other_installment_plans | categorical | Other installment/financing plans the applicant has (bank, stores, or none).                                                                                    |
| housing                 | categorical | Housing situation (rent, own, or living for free).                                                                                                              |
| n_credits               | numerical   | Number of existing credits/loans held by the applicant (count).                                                                                                 |
| job                     | categorical | Job/occupation skill level category (e.g., unemployed/unskilled to management/highly qualified).                                                                |
| n_guarantors            | numerical   | Number of people liable to provide maintenance/guarantees (count of dependents/obligations as represented in the dataset).                                      |
| telephone               | categorical | Whether the applicant has a telephone registered in their name (none vs yes).                                                                                   |
| is_foreign_worker       | categorical | Whether the applicant is classified as a foreign worker (yes/no).                                                                                               |


### Taiwan Credit Risk Dataset
- **Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients)
- **Description**: Contains information on default payments, demographic factors, credit data, payment history, and bill statements of credit card clients in Taiwan from April 2005 to September 2005.
- **Link**: https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients

##### Fields
| column_name | type        | description                                                                                                                             |
| ----------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| id          | numerical   | Unique identifier for each credit card client.                                                                                          |
| limit_bal   | numerical   | Total credit limit granted to the customer (NT dollars), including both individual and family/supplementary credit.                     |
| sex         | categorical | Gender of the client (1 = male, 2 = female).                                                                                            |
| education   | categorical | Highest level of education attained (1 = graduate school, 2 = university, 3 = high school, 4 = others).                                 |
| marriage    | categorical | Marital status (1 = married, 2 = single, 3 = others).                                                                                   |
| age         | numerical   | Age of the client in years.                                                                                                             |
| pay_0       | categorical | Repayment status in **September 2005** (−1 = paid duly; 1 = one-month delay; 2 = two-month delay; …; 9 = nine months or more of delay). |
| pay_2       | categorical | Repayment status in **August 2005** using the same delay scale.                                                                         |
| pay_3       | categorical | Repayment status in **July 2005** using the same delay scale.                                                                           |
| pay_4       | categorical | Repayment status in **June 2005** using the same delay scale.                                                                           |
| pay_5       | categorical | Repayment status in **May 2005** using the same delay scale.                                                                            |
| pay_6       | categorical | Repayment status in **April 2005** using the same delay scale.                                                                          |
| bill_amt1   | numerical   | Amount of bill statement in **September 2005** (NT dollars).                                                                            |
| bill_amt2   | numerical   | Amount of bill statement in **August 2005** (NT dollars).                                                                               |
| bill_amt3   | numerical   | Amount of bill statement in **July 2005** (NT dollars).                                                                                 |
| bill_amt4   | numerical   | Amount of bill statement in **June 2005** (NT dollars).                                                                                 |
| bill_amt5   | numerical   | Amount of bill statement in **May 2005** (NT dollars).                                                                                  |
| bill_amt6   | numerical   | Amount of bill statement in **April 2005** (NT dollars).                                                                                |
| pay_amt1    | numerical   | Amount paid in **September 2005** (NT dollars).                                                                                         |
| pay_amt2    | numerical   | Amount paid in **August 2005** (NT dollars).                                                                                            |
| pay_amt3    | numerical   | Amount paid in **July 2005** (NT dollars).                                                                                              |
| pay_amt4    | numerical   | Amount paid in **June 2005** (NT dollars).                                                                                              |
| pay_amt5    | numerical   | Amount paid in **May 2005** (NT dollars).                                                                                               |
| pay_amt6    | numerical   | Amount paid in **April 2005** (NT dollars).                                                                                             |
| target      | categorical | Default indicator for the following month (1 = default, 0 = no default).                                                                |
| _is_test    | categorical | Flag indicating whether the record belongs to the test split (True = test set, False = training/validation set).                        |
