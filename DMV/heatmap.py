import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Ground_Averages.csv")
numeric_columns = [
    "Mat",
    "Won",
    "Tied",
    "NR",
    "Runs",
    "Wkts",
    "Balls",
    "Ave",
    "RPO"
]
correlation = df[numeric_columns].corr()
plt.figure(figsize=(12, 9))
sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5
)
plt.title("Correlation Heatmap of Cricket Statistics")
plt.tight_layout()
plt.show()