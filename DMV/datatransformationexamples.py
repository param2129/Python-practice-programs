import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
df = pd.read_csv('transformation_sample_data.csv')
print("Original Dataset Preview:")
print(df.head(), "\n" + "-"*50)
scaler = StandardScaler()
df['income_standardized'] = scaler.fit_transform(df[['annual_income']])
minmax_scaler = MinMaxScaler()
df['score_normalized'] = minmax_scaler.fit_transform(df[['score']])
df['income_log'] = np.log1p(df['annual_income'])
rating_mapping = {'Low': 1, 'Medium': 2, 'High': 3}
df['performance_encoded'] = df['performance_rating'].map(rating_mapping)
df = pd.get_dummies(df, columns=['department'], prefix='dept', dtype=int)
bins = [18, 30, 45, 70]
labels = ['Young', 'Middle-Aged', 'Senior']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, include_lowest=True)
print("Transformed Dataset Preview:")
print(df[['annual_income', 'income_standardized', 'income_log', 'performance_encoded', 'age_group']].head())
