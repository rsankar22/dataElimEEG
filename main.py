import pandas as pd

df = pd.read_csv('EEGRaw.csv')
ya_only = df[23920:]
#ya_only = ya_only.drop(['Condition','Channel'], axis = 1)
#ya_only.to_csv('Converted.csv')
#print(ya_only)




# add conversion portion below focus on iterations and text to int conversion
df_edit = pd.read_csv('Edited_Convert.csv')
print(df_edit)
condition = ['CHN','HGH','LOW','HRD']
for i in df_edit.Condition:
    if i == 'CHN':
        df_edit.Condition[i] = 1
    elif i == 'HGH':
        df_edit.Condition[i] = 2
    elif i == 'LOW':
        df_edit.Condition[i] = 3
    elif i == 'HDR':
        df_edit.Condition[i] = 4


