import numpy as np
import pandas as pd

from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
statlog_german_credit_data = fetch_ucirepo(id=144) 

field_mapping = {
    'Attribute1': 'status_account', #qualitative
    'Attribute2': 'month_duration', #numerical
    'Attribute3': 'credit_history', #qualitative
    'Attribute4': 'purpose', #qualitative
    'Attribute5': 'credit_amount', #numerical
    'Attribute6': 'status_savings', #qualitative
    'Attribute7': 'years_employment', #qualitative
    'Attribute8': 'payment_to_income_ratio', #numerical
    'Attribute9': 'status_and_sex', #qualitative
    'Attribute10': 'secondary_obligor', #qualitative
    'Attribute11': 'residence_since', #numerical
    'Attribute12': 'collateral', #qualitative
    'Attribute13': 'age', #numerical
    'Attribute14': 'other_installment_plans', #qualitative
    'Attribute15': 'housing', #qualitative
    'Attribute16': 'n_credits', #numerical
    'Attribute17': 'job', #qualitative
    'Attribute18': 'n_guarantors', #numerical
    'Attribute19': 'telephone', #qualitative
    'Attribute20': 'is_foreign_worker' #qualitative     
}

value_mapping = {
    'status_account': {
        'A11': '< 0 DM',
        'A12': '0 to < 200 DM',
        'A13': '>= 200 DM',
        'A14': 'no checking account'
    },

    'credit_history': {
        'A30': 'no credits taken/ all credits paid back duly',
        'A31': 'all credits at this bank paid back duly',
        'A32': 'existing credits paid back duly till now',
        'A33': 'delay in paying off in the past',
        'A34': 'critical account/ other credits existing (not at this bank)'
    },

    'purpose': {
        'A40': 'car (new)',
        'A41': 'car (used)',
        'A42': 'furniture/equipment',
        'A43': 'radio/television',
        'A44': 'domestic appliances',
        'A45': 'repairs',
        'A46': 'education',
        'A47': 'vacation',
        'A48': 'retraining',
        'A49': 'business',
        'A410': 'others'
    },

    'status_savings': {
        'A61': '< 100 DM',
        'A62': '100 to < 500 DM',
        'A63': '500 to < 1000 DM',
        'A64': '>= 1000 DM',
        'A65': 'unknown/ no savings account'
    },

    'years_employment': {
        'A71': 'unemployed',
        'A72': '< 1 year',
        'A73': '1 to < 4 years',
        'A74': '4 to < 7 years',
        'A75': '>= 7 years'
    },

    'status_and_sex':{
        'A91': 'male : divorced/separated',
        'A92': 'female : divorced/separated/married',
        'A93': 'male : single',
        'A94': 'male : married/widowed',
        'A95': 'female : single'
    },

    'secondary_obligor': {
        'A101': 'none',
        'A102': 'co-applicant',
        'A103': 'guarantor'
    },
    
    'collateral': {
        'A121': 'none',
        'A122': 'car',
        'A123': 'real estate',
        'A124': 'savings agreement/life insurance'
    },

    'other_installment_plans': {
        'A141': 'bank',
        'A142': 'stores',
        'A143': 'none'
    },

    'housing': {
        'A151': 'rent',
        'A152': 'own',
        'A153': 'for free'
    },

    'job': {
        'A171': 'unemployed/ unskilled - non-resident',
        'A172': 'unskilled - resident',
        'A173': 'skilled employee/ official',
        'A174': 'management/ self-employed/highly qualified employee'
    },

    'telephone': {
        'A191': 'none',
        'A192': 'yes, registered under the customers name'
    },

    'is_foreign_worker': {
        'A201': 'yes',
        'A202': 'no'
    },

    'target': {
        1: 'good',
        2: 'bad'
    }
}


df_feat = statlog_german_credit_data['data']['features'].copy()
df_y = statlog_german_credit_data['data']['targets'].copy()
# store the raw data
pd.concat([df_feat, df_y], axis=1).to_csv('../data/raw/raw_german_credit_data.csv', index=False)

df_feat = df_feat.rename(columns=field_mapping, inplace=False)

for col in df_feat:
    if col in value_mapping:
        df_feat[col] = df_feat[col].map(value_mapping[col])


df_y.columns = ['target']
df_y['target'] = df_y['target'].map(value_mapping['target'])

out_df = pd.concat([df_feat, df_y], axis=1)

rng = np.random.default_rng(42)
out_df['_is_test'] = rng.random(len(out_df)) > 0.75   # 75% train

out_df.to_csv('../data/german_credit_data.csv', index=False)