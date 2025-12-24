import numpy as np
import pandas as pd

df = pd.read_excel("../data/raw/raw_taiwan_credit_card.xls", header=1)

df.rename(
    columns={"default payment next month": "target"}, 
    inplace=True)

df.columns = [col.replace(' ', '').lower() for col in df.columns]

rng = np.random.default_rng(42)
df['_is_test'] = rng.random(len(df)) > 0.75   # 75% train

df.to_csv("../data/taiwan_credit_card.csv", index=False)