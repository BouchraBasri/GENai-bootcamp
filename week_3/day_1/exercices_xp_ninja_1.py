# %%
# Exercice 1

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Mall_customers = pd.read_csv("data/Mall_Customers.csv")

Mall_customers.head()
# %%
Mall_customers.info()
# %%
Mall_customers.shape
# %%
Mall_customers.columns
# %%
Mall_customers.describe()
# %%
Mall_customers.describe(include=["object"])
# %%
Mall_customers.isnull().sum()
# %%
Mall_customers[Mall_customers.duplicated()]
# %%
plt.figure(figsize=(10,6))
sns.pairplot(data=Mall_customers)
plt.show()
# %%
plt.figure(figsize=(10,6))
sns.histplot(Mall_customers["Spending Score (1-100)"], kde=True, color="red")
plt.title("Spending Score Distribution")
plt.xlabel("Spending Score")
plt.ylabel("Density")
plt.show()
# %%
plt.figure(figsize=(10,6))
sns.histplot(Mall_customers["Age"])
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Density")
plt.show()
# %%
plt.figure(figsize=(10,6))
plt.histplot(Mall_customers["Annual Income (k$)"], color = 'y')
plt.title('Annual Income Distribution')
plt.show()
# %%
plt.figure(figsize = (10,6))
sns.boxplot(Mall_customers["Spending Score (1-100)"])
plt.title('Spending Score Distribution')
plt.show()
# %%
plt.figure(figsize = (10,6))
sns.boxplot(Mall_customers["Age"])
plt.title('Age Distribution')
plt.show()
# %%
plt.figure(figsize = (10,6))
sns.boxplot(Mall_customers["Annual Income (k$)"])
plt.title('Annual Income (k$) Distribution')
plt.show()
# %%
plt.figure(figsize=(10,6))
sns.countplot(x = 'Gender', data = Mall_customers, palette="plasma")
plt.title('Total Number of Male and Female')
plt.xlabel('Gender')
plt.show()
# %%
plt.figure(figsize = (10,6))
sns.scatterplot(x='Age',y='Annual Income (k$)',color='r',data=Mall_customers, hue="Gender")
plt.title('Age vs Annual Income (k$)',size=18)
plt.xlabel('Age',size=14)
plt.ylabel('Annual Income (k$)',size=14)
plt.show()
# %%
df_num = Mall_customers.select_dtypes(include=[int, float])
print(df_num)
# %%
print('Correlation between age and annual income is : {}'.format(
    round(df_num.corr()['Age']['Annual Income (k$)'], 3)
))

# %%
plt.figure(figsize = (10,6))
sns.heatmap(df_num.corr(),annot=True)
plt.title('Correlations Between Variables')
plt.show()
# %%
