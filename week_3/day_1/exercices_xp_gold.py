# %%
# Exercice 1
import math
number = 9
if number > 1:
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            print(f"{number} is not a prime number.")
            break
    else:
        print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
        
# %%
# Exercice 2
start = 1
end = 20
divisor = 3

divisible_numbers = [num for num in range(start, end + 1) if num % divisor == 0]

print(divisible_numbers)
# %%
#Exercice 3
import pandas as pd

df = pd.read_csv("data/Iris.csv")

df.head()
# %%
df.columns
# %%
df.dtypes
# %%
# Exercice 4
import pandas as pd

df = pd.read_csv("data/Iris.csv")
# %%
mean_value = df["PetalWidthCm"].mean()
print(mean_value)
# %%
median_value = df["PetalWidthCm"].median()
print(median_value)
# %%
mode_value = df["PetalWidthCm"].mode()[0]
print(mode_value)
# %%
# Exercice 5
import pandas as pd

df = pd.read_csv("data/titanic.csv")
df.head()
# %%
df["Sex"] = df["Sex"].map({"female": 0, "male": 1})
df.head()
# %%
