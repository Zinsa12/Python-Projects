import pandas as pd
df = pd.read_csv("vk.csv")
print(df.head())
print(df.tail())
# df = pd.read_excel("student(xlsx).xlsx",sheet_name="Project Management Data")



df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40]
})

# Creating second DataFrame
df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'Salary': [50000, 60000, 70000, 80000]
})

# Performing Inner Join
merged_df = pd.merge(df1, df2, on='ID')

print(merged_df)
left_df = pd.merge(df1, df2, on='ID',how='left')
print(left_df)
right_df = pd.merge(df1, df2, on='ID',how='right')
print(right_df)
outer_df = pd.merge(df1, df2, on='ID',how='outer')
print(outer_df)


# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Age': [25, 30, 35, 40, 29],
    'Salary': [50000, 60000, 70000, 80000, 55000]
}

df = pd.DataFrame(data)

# Summary statistics
print(df.describe())
df.plot(kind="bar", x="Name", y="Salary", color="skyblue", title="Salary Distribution")

# Sample data
data = {
    "Date": ["2024-01-01", "2024-01-01", "2024-01-02", "2024-01-02"],
    "Product": ["Laptop", "Mouse", "Laptop", "Mouse"],
    "Sales": [1200, 100, 1300, 120],
}

df = pd.DataFrame(data)

# Pivot the DataFrame
pivot_df = df.pivot(index="Date", columns="Product", values="Sales")
print(pivot_df)
data = {
    "Store": ["A", "A", "B", "B", "A", "B"],
    "Product": ["Laptop", "Mouse", "Laptop", "Mouse", "Laptop", "Mouse"],
    "Sales": [1200, 100, 1300, 120, 1400, 130],
}

df = pd.DataFrame(data)

# Pivot Table with Mean Sales
pivot_table_df = df.pivot_table(index="Store", columns="Product", values="Sales", aggfunc="mean")
print(pivot_table_df)

sales = pd.DataFrame({
    'Region': ['East', 'West', 'East', 'South', 'West'],
    'Sales': [2500, 3000, 1800, 2200, 3500]
})

print(sales.groupby('Region')['Sales'].sum())


print(sales.groupby('Region')['Sales'].agg(['mean', 'max', 'min']))