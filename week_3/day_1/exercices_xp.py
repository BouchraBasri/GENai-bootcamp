# %%
# Exercices 2 & 3
import pandas as pd

df = pd.read_csv("data/sleep_health.csv")
df.head()

# This dataset provides information about the sleeping habits of Americans across different demographic groups.
# Year = quantitative
# Period = qualitative
# Avg hrs per day = quatitative
# Standard error = quantitative 
# Type of days = qualitative
# Age group = qualitative
# Activity = qualitative
# Sex = qualitative
# %%
df = pd.read_csv("data/mental_health.csv")
df.head()

# This dataset contains worldwide statistics on mental health disorders over time.
# Entity = qualitative
# Code = qualitative
# Year = quantitative
# Schizophrenia = quantitative
# Bipolar disorder = quantitative
# Eating disorders = quantitative
# Anxiety disorders = quantitative
# Depression = quantitative
# Alcohol use disorders = quantitative
# %%
df = pd.read_csv("data/application_record.csv")
df.head()
print(df)

# This dataset includes demographic and financial information about individuals applying for credit cards.
# Gender = qualitative
# Age = quantitative
# Debt = quantitative
# Married = qualitative
# BankCustomer = quanlitative
# Industry = qualitative
# Ethnicity = qualitative
# YearsEmployed = quantitative
# PeriodrDefault = qualitative
# Employed = qualitative
# CreditScore = quantitative
# DriversLicense = qualitative
# Citizen = qualitative
# ZipCode = qualitative
# Income = quantitative
# Approved = qualitative
# %%
# Exercice 4
import pandas as pd

df = pd.read_csv("data/Iris.csv")
# %%
df.head()
# %%
df.columns
# %%
qualitative = []
quantitative = []

for col in df.columns:
    if df[col].dtype == "object":
        qualitative.append(col)
    else:
        quantitative.append(col)

print("Quantitative columns: ")
print(quantitative)
print("Qualitative columns: ")
print(qualitative)
# Explanation of each column:

# Id:
#   Quantitative — numeric identifier, but not a real measurement.

# SepalLengthCm:
#   Quantitative — continuous numeric measurement in centimeters.

# SepalWidthCm:
#   Quantitative — continuous numeric measurement in centimeters.

# PetalLengthCm:
#   Quantitative — numeric measurement in centimeters.

# PetalWidthCm:
#   Quantitative — numeric measurement in centimeters.

# Species:
#   Qualitative — categorical variable (setosa, versicolor, virginica).

# %%
mean_value = df["PetalWidthCm"].mean()
median_value = df["PetalWidthCm"].median()
mode_value = df["PetalWidthCm"].mode()[0]
print(mean_value)
print(median_value)
print(mode_value)

# %%
# Exercice 5
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8,5))
sns.histplot(df["PetalLengthCm"], bins=20)
plt.title("Distribution of Petal length")
plt.xlabel("Petal length (cm)")
plt.ylabel("Frequency")
plt.show()
# %%
# Exercice 6
df = pd.read_csv("data/sleep_health.csv")
df.head()
# YEAR:
# Useful for Trend Analysis.

# Avg hrs per day:
# Perfect for Trend Analysis, Comparisin groups, and Statistical calculations.

# Age Group:
# Useful for group comparisons.

# Sex:
# Useful for demographic comparisons.

# Type of Days:
# Enables analysis based on the type of the day.

# Period:
# Useful for distinguisheing different time intervals.
# %%
