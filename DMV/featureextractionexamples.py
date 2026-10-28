import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import PCA
df = pd.read_csv('feature_extraction_sample.csv')
print("Original Dataset Preview:")
print(df.head(2), "\n" + "-"*50)
count_vec = CountVectorizer(stop_words='english')
bow_matrix = count_vec.fit_transform(df['review_text'])
print(f"Bag-of-Words Matrix Shape: {bow_matrix.shape}")
tfidf_vec = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vec.fit_transform(df['review_text'])
print(f"TF-IDF Matrix Shape: {tfidf_matrix.shape}")
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
df['day_of_week'] = df['timestamp'].dt.dayofweek
df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
df['sensor_sum'] = df['sensor_reading_1'] + df['sensor_reading_2']
df['sensor_ratio'] = df['sensor_reading_1'] / (df['sensor_reading_2'] + 1e-5)
pca = PCA(n_components=1)
df['sensor_pca'] = pca.fit_transform(df[['sensor_reading_1', 'sensor_reading_2']])
print("\nExtracted Features Dataset Preview:")
print(df[['hour', 'is_weekend', 'sensor_sum', 'sensor_ratio', 'sensor_pca']].head())
