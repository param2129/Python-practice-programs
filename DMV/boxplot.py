from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
csv_path = Path(__file__).resolve().parent.parent / "Ground_Averages.csv"
df = pd.read_csv(csv_path)
columns = ["Runs", "Wkts", "Ave"]
plt.figure(figsize=(10, 6))
plt.boxplot(
    [df[column].dropna() for column in columns],
    patch_artist=True
)
plt.xticks(range(1, len(columns) + 1), columns)
plt.title("Distribution of Cricket Performance Statistics")
plt.xlabel("Performance Statistics")
plt.ylabel("Values")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()