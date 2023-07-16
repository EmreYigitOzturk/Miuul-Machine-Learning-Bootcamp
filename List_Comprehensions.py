import seaborn as sns
df = sns.load_dataset("car_crashes")
list = []
for i in df.columns:
    list.append("NUM_"+i.upper())

list
list2=[]

for i in df.columns:
    if "no" in i:
        list2.append(i.upper())
    else:
        list2.append(i.upper() + "_FLAG")

list2
[list2.append(i.upper() + "_FLAG") if "no" not in i  else list2.append(i.upper()) for i in df.columns]

og_list = ["abbrev","no_previous"]
new_df = df.columns.drop(og_list)
df[new_df].head()
