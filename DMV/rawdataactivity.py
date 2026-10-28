import pandas as pd
import numpy as np

print("--- 1. LOADING DATASET ---")
df = pd.read_csv('rawcustomerdata.csv')
print(f"Initial shape: {df.shape}")
print(df.head())
print("\n--- 2. INITIAL INSPECTION ---")
print(df.info())
print("\nMissing values count per column:")
print(df.isnull().sum())
print("\n--- 3. REMOVING DUPLICATES ---")
initial_rows = len(df)
df = df.drop_duplicates().reset_index(drop=True)
print(f"Removed {initial_rows - len(df)} duplicate rows. New shape: {df.shape}")

print("\n--- 4. HANDLING MISSING VALUES ---")

df['age'] = df['age'].fillna(df['age'].median())
df['total_purchases'] = df['total_purchases'].fillna(0)


df['gender'] = df['gender'].fillna('Unknown')
df['account_status'] = df['account_status'].fillna('Unknown')

df = df.dropna(subset=['signup_date', 'customer_id'])
print("Missing values after cleaning:")
print(df.isnull().sum())

print("\n--- 5. FORMATTING & TEXT CLEANING ---")

df['account_status'] = df['account_status'].str.strip().str.title()

gender_mapping = {'M': 'Male', 'F': 'Female', 'other': 'Other'}
df['gender'] = df['gender'].replace(gender_mapping).str.title()

df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce')

df = df.dropna(subset=['signup_date'])

print("\n--- 6. OUTLIER DETECTION & TREATMENT ---")

print(f"Rows before age filtering: {len(df)}")
df = df[(df['age'] >= 18) & (df['age'] <= 100)]

Q1 = df['income'].quantile(0.25)
Q3 = df['income'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df['income'] = np.where(df['income'] > upper_bound, upper_bound, df['income'])
df['income'] = np.where(df['income'] < lower_bound, lower_bound, df['income'])
print(f"Rows after outlier filtering: {len(df)}")

print("\n--- 7. FINAL ML PREPARATION ---")
# Extract date features
df['signup_year'] = df['signup_date'].dt.year
df['signup_month'] = df['signup_date'].dt.month

df_cleaned = pd.get_dummies(df, columns=['gender', 'account_status'], drop_first=True)

print("\n--- CLEANED DATASET PREVIEW ---")
print(df_cleaned.head())
print(f"Final cleaned shape: {df_cleaned.shape}")

df_cleaned.to_csv('cleaned_customer_data.csv', index=False)
print("\nCleaned dataset saved successfully to 'cleaned_customer_data.csv'.")
