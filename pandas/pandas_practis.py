from multiprocessing.reduction import duplicate

import numpy as np
import pandas as pd

np.random.seed(42)

data = [
    {"Name": "Alice", "Age": 25, "City": "New York"},
    {"Name": "Bob", "Age": 30, "City": "London"},
    {"Name": "Charlie", "Age": 22, "City": "Paris"}
]
df = pd.DataFrame(data)
df["Salary"] = [50000, 60000, 45000]
print(df)


df.loc[3] = ["David", 27, "Berlin",9]
print(df)

print("\n",df[df["Age"] == 25])
print("\n",df[["Name","Age"]])

df["Salary"] = [50000, None, 45000,None]
print(df.isnull())
print(df.fillna(value=df["Salary"].sum(), inplace=True))
print(df.sort_values(by="Age", ascending=False))  # Sort by Age (descending)


data = {
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "Department": ["HR", "IT", "IT", "Finance", "HR", "Finance"],
    "Salary": [50000, 70000, 75000, 60000, 52000, 58000]
}

df = pd.DataFrame(data)
num_employees = df.shape[1]
print("Total Employees:", num_employees)

print(df["Department"].value_counts())

df["bo"] = df["Salary"] * 0.10
print(df)
print(df.groupby("Department")["Salary"].value_counts())
print(df.groupby("Department")["Salary"].mean())
print(df.sort_values(by="Department",ascending=False))
print(df["Department"].replace("IT","Information Technology"))

duplicate1 = df.duplicated(subset="Department")
print(duplicate1.any())
print(duplicate1)
df.to_csv("D:\python\pandas\pandas_practis.csv")