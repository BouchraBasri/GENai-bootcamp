# %%
# Exercice 2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%%
df = pd.read_csv("data/titanic.csv")

# %%
df.head()
# %%
df.info
# %%
df.describe()
#%%
df.dtypes
#%%
df.columns
# %%
df.isnull().sum()
# %%
df['Age'] = df['Age'].fillna(df['Age'].median())
# %%
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
# %%
df['Cabin'] = df['Cabin'].fillna("Unknown")
# %%
df['Sex'] = df['Sex'].map({'male':1, 'female':0})
# %%
df['Embarked'] = df['Embarked'].map({'S':2, 'C':1, 'Q':0})

# %%
df["Embarked"].unique()
# %%
plt.figure(figsize=(10,6))
sns.histplot(df['Age'])
plt.title("Age Distribution")
plt.xlabel("Age")
plt.show()
# %%
plt.figure(figsize=(10,6))
sns.histplot(df['Fare'], kde=True)
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.show()
# %%
plt.figure(figsize=(10,6))
sns.countplot(x='Survived', data=df, palette='plasma')
plt.title("Survival Count")
plt.xlabel("Survived")
plt.ylabel("Count")
plt.xticks([0, 1], ['Died', 'Survived'] )
plt.show()
# %%
plt.figure(figsize=(10,6))
sns.countplot(x='Sex', data=df, palette='pastel')
plt.title("Gender Count")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.xticks([0,1], ['Female', 'male'])
plt.show()
# %%
plt.figure(figsize=(20,8))
sns.barplot(x='Pclass', y='Survived', data=df, palette='plasma')
plt.title("Survival Rate by Ticket Class")
plt.xlabel('PClass')
plt.ylabel('Survived')
plt.show()
#1st-class passengers had the highest survival rate, followed by 2nd class.While 3rd-class passengers had the lowest survival, showing a clear socioeconomic divide.
# %%
plt.figure(figsize=(20,8))
sns.barplot(x='Sex', y='Survived', data=df, palette='plasma')
plt.title("Survival Rate by Gender")
plt.xlabel('Gender')
plt.ylabel('Survived')
plt.xticks([0,1], ['Male', 'Female'])
plt.show()
#Females had a significantly higher survival rate than males.
# %%
plt.figure(figsize=(20,8))
sns.boxplot(x='Survived', y='Age', data=df)
plt.title('Age vs Survival')
plt.show()
# %%
plt.figure(figsize=(10,6))
sns.catplot(x='Pclass', y='Survived', hue='Sex', kind='bar', data=df)
plt.title("Survival Rate by Class and Sex")
plt.xticks([0,1], ['Male', 'Female'])
plt.show()
# %%
df['Survived_label'] = df['Survived'].map({0: 'Died', 1: 'Survived'})
df['Sex_label'] = df['Sex'].map({1: 'Male', 0: 'Female'})

plt.figure(figsize=(10,6))
sns.scatterplot(x='Age', y='Fare', data=df, hue='Sex_label', style='Survived_label')
plt.show()
# %%
df_num = df.select_dtypes(include=['int64', 'Float64'])

plt.figure(figsize=(10,6))
sns.heatmap(df_num.corr(), annot=True)
plt.show()
