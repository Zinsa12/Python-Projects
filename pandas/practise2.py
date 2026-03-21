import pandas as pd

data = {
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack"],
    "Department": ["HR", "IT", "IT", "Finance", "HR", "Finance", "IT", "HR", "Finance", "IT"],
    "Salary": [50000, 70000, 75000, 60000, 52000, 58000, 80000, 55000, 62000, 90000],
    "Expi": [5, 8, 6, 10, 4, 9, 7, 3, 11, 15],
    "Rating": [3, 4, 5, 4, 3, 4, 5, 2, 5, 5]
}

df = pd.DataFrame(data)
print(df)
eligible = df[(df["Expi"] >= 7) & (df["Rating"] >= 4)]
print(eligible)

avg_salary = df.groupby("Department")["Salary"].mean()
print(avg_salary)

print(df.nlargest(3,"Salary"))
df["tax"] = df["Salary"] * 0.10
print(df)
print(df.isnull().sum())
best_dept = df.groupby("Department")["Rating"].mean().idxmax()
print("Department with Highest Performance:", best_dept)
df.to_csv("D:\python\pandas\practis2.csv", index=False)
