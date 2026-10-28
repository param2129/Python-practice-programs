import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Ground_Averages.csv" )
top_grounds = df.sort_values("Runs", ascending=False).head(15)
plt.figure(figsize=(14, 7))
plt.bar(
    top_grounds["Ground"],
    top_grounds["Runs"]
)
plt.title("Top 15 Grounds by Runs")
plt.xlabel("Ground")
plt.ylabel("Runs")
plt.xticks(rotation=75, ha="right")
plt.tight_layout()
plt.show()