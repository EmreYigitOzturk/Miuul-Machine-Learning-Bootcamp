import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
#df.head()

#sns.countplot(x=df["sex"],data=df)
#df.plot.barh()

sns.scatterplot(x=df["tip"],y=df["total_bill"],hue=df["smoker"],data=df)


plt.show()

def calc(w,h):
    print(w*h)

calc(10,40)-200

import numpy as np
from functools import reduce

num_l= np.arange(10)

filter_l = list(filter(lambda x: x%3 == 0,num_l))

final_l = reduce(lambda x,y: x * y,filter_l)
final_l
import seaborn as sns
df = sns.load_dataset("titanic")
df[["sex","survived"]].groupby("sex").mean()