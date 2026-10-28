import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Ground_Averages.csv")
plt.figure(figsize=(12, 8))
plt.scatter(
    df["Mat"],
    df["Runs"],
    s=df["Wkts"] * 8,
    alpha=0.6
)
plt.title("Matches vs Runs with Wickets as Bubble Size")
plt.xlabel("Number of Matches")
plt.ylabel("Runs")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()