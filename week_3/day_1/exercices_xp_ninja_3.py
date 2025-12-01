#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%%
df = pd.read_csv('data/Iris.csv')

#%%
df.head()
# %%
df.info()
# %%
df.describe()
# %%
df.columns
# %%
df['Species'].unique()
#%%
df['Species'].value_counts()
# %%
plt.figure(figsize=(10,6))
sns.histplot(df['SepalLengthCM'])
plt.title('')
plt.show()
# %%
