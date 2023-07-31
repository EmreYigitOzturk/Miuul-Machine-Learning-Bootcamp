import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import missingno as msno
from datetime import date
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import MinMaxScaler, LabelEncoder, StandardScaler, RobustScaler

df = pd.read_csv("datasets/diabetes.csv")
df.head()

num_col = [col for col in df.columns if df[col].dtype != 'O' ]
num_but_cat = [col for col in df.columns if df[col].dtype != 'O' and df[col].nunique()<10]
num_col = [col for col in num_col if col != 'Outcome']
cat_cols = [col for col in df.columns if df[col].dtype == 'O']
cat_cols = cat_cols + num_but_cat
df['Outcome'].head()
df.isnull().any()

def outlier_thresholds(dataframe, col_name, q1=0.25, q3=0.75):
    quartile1 = dataframe[col_name].quantile(q1)
    quartile3 = dataframe[col_name].quantile(q3)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return low_limit, up_limit


def check_outlier(dataframe, col_name):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name)
    if dataframe[(dataframe[col_name] > up_limit) | (dataframe[col_name] < low_limit)].any(axis=None):
        return True
    else:
        return False
low_limit, up_limit = outlier_thresholds(df, 'Pregnancies')
df.shape
check_outlier(df,"Pregnancies")
df[(df['Pregnancies']<low_limit) | (df['Pregnancies']>up_limit)].index
df[~((df['Pregnancies']<low_limit) | (df['Pregnancies']>up_limit))].shape

df.loc[(df['Pregnancies']<low_limit), 'Pregnancies'] = low_limit
df.loc[(df['Pregnancies']>up_limit), 'Pregnancies'] = up_limit

def replace_with_thresholds(df,variable):
    low_limit , up_limit = outlier_thresholds(df,variable)
    df.loc[(df[variable] < low_limit), variable] = low_limit
    df.loc[(df[variable] > up_limit), variable] = up_limit

for col in num_col:
    print(col,check_outlier(df,col))

for col in num_col:
    replace_with_thresholds(df,col)
df.head()

df.columns
df.isnull().any()
dff = df.drop("Outcome",axis=1).copy()
dff[dff.isin([0])] = None
dff.head()
dff["Outcome"] = df["Outcome"]
#Missing Value
for col in num_col:
    dff[col].fillna(dff[col].mean(),inplace=True)


#Encoding
le = LabelEncoder()
le.fit_transform(dff["Outcome"])[0:5]
#Standart Scaler
scaler = StandardScaler()
dff[num_col] = scaler.fit_transform(dff[num_col])
dff[num_col].head()
#Model
y = dff["Outcome"]
X = dff.drop("Outcome",axis=1)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=17)

from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(random_state=46).fit(X_train, y_train)
y_pred = rf_model.predict(X_test)
accuracy_score(y_pred, y_test)

def plot_importance(model, features, num=len(X), save=False):
    feature_imp = pd.DataFrame({'Value': model.feature_importances_, 'Feature': features.columns})
    plt.figure(figsize=(10, 10))
    sns.set(font_scale=1)
    sns.barplot(x="Value", y="Feature", data=feature_imp.sort_values(by="Value",
                                                                      ascending=False)[0:num])
    plt.title('Features')
    plt.tight_layout()
    plt.show()
    if save:
        plt.savefig('importances.png')


plot_importance(rf_model, X_train)


