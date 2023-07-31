import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df["sex"].value_counts()

for col in df.columns:
    print({col: df[col].nunique()})

df[["pclass", "parch"]].nunique()
str(df['embarked'].dtype)
df["embarked"].value_counts()

df[df["embarked"] == "C"]

df[df["embarked"] != "S"]
df[(df["age"] < 30) & (df["sex"] == "female")]
df[(df["fare"] > 500) | (df['age'] > 70)]
df.isnull().sum()
new_df = df.drop("who", axis=1)
new_df.columns

df["deck"].mode()
df["deck"].fillna(df["deck"].mode()[0], inplace=True)
df["age"].median()
df['age'].fillna(df['age'].median(), inplace=True)
df.head()
df['age']

df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "count", "mean"]})


def flag_age_group(age):
    if age < 30:
        return 1
    else:
        return 0


df["age_flag"] = df['age'].apply(lambda age: 1 if age < 30 else 0)

df = sns.load_dataset("tips")

df.groupby(["time"]).agg({"total_bill": ["sum","min","max","mean"]})
df.groupby(["time","day"]).agg({"total_bill": ["sum","min","max","mean"]})
df.groupby([(df["time"] == "Lunch") & (df["sex"] == "Female")]).agg({"total_bill": ["sum","min","max","mean"]})
df_data = df[(df["time"] == "Lunch") & (df["sex"] == "Female")]

df_data.groupby("day").agg({"total_bill" : ["sum","min","max","mean"]})

df.loc[(df["size"]<3) & (df["total_bill"]>10)]
df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]

df.sort_values(by='total_bill_tip_sum', ascending=False).head(30)

df.mode()
df.head()
