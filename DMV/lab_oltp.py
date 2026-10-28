import pandas as pd
# Create the DataFrame:
data = {
'Date': [
'2026-01-10','2026-01-15','2026-02-05',
'2026-02-12','2026-03-10','2026-03-15',
'2026-04-02','2026-04-18','2026-05-05',
'2026-05-20'
],
'Region': [
'South','South','South','North','North',
'South','East','North','South','East'
],
'Category': [
'Electronics','Electronics','Furniture',
'Electronics','Furniture','Electronics',
'Electronics','Electronics','Furniture',
'Electronics'
],
'Product': [
'Laptop','Mobile','Chair','Laptop','Table',
'Laptop','Mobile','Mobile','Table','Laptop'
],
'Sales': [
60000,30000,15000,90000,40000,
120000,50000,70000,30000,80000
],
'Quantity': [
2,3,5,3,4,4,5,7,3,2
]
}
df = pd.DataFrame(data)
print(df)

df.groupby('Region')['Sales'].sum()

import matplotlib.pyplot as plt

# Convert Date column into datetime format
df['Date'] = pd.to_datetime(df['Date'])

# ---------------- BAR CHART ----------------
# Total Sales by Region
region_sales = df.groupby('Region')['Sales'].sum()

plt.figure(figsize=(8, 5))
plt.bar(region_sales.index, region_sales.values)
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ---------------- HISTOGRAM ----------------
# Distribution of Sales
plt.figure(figsize=(8, 5))
plt.hist(df['Sales'], bins=5, edgecolor='black')
plt.title('Distribution of Sales')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()


# ---------------- LINE CHART ----------------
# Sales Trend over Time
date_sales = df.groupby('Date')['Sales'].sum()

plt.figure(figsize=(10, 5))
plt.plot(date_sales.index, date_sales.values, marker='o')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


# ---------------- PIE CHART ----------------
# Sales Distribution by Category
category_sales = df.groupby('Category')['Sales'].sum()

plt.figure(figsize=(7, 7))
plt.pie(
    category_sales.values,
    labels=category_sales.index,
    autopct='%1.1f%%',
    startangle=90
)
plt.title('Sales Distribution by Category')
plt.tight_layout()
plt.show()