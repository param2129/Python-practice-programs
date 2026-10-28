import pandas as pd
import matplotlib.pyplot as plt

# Read CSV dataset
df = pd.read_csv("attendanceactivity.csv")

# Display first 5 records
print("First 5 Records:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# -------------------------------
# 1. Line Chart
# -------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    df["Student_ID"],
    df["Activity_Score"],
    marker="o",
    linestyle="-"
)

plt.title("Student Activity Score")
plt.xlabel("Student ID")
plt.ylabel("Activity Score")
plt.grid(True)

plt.show()


# -------------------------------
# 2. Bar Chart
# -------------------------------

plt.figure(figsize=(10, 6))

plt.bar(
    df["Student_ID"],
    df["Activity_Score"]
)

plt.title("Activity Score by Student")
plt.xlabel("Student ID")
plt.ylabel("Activity Score")
plt.xticks(rotation=45)

plt.show()


# -------------------------------
# 3. Histogram
# -------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    df["Activity_Score"],
    bins=10,
    edgecolor="black"
)

plt.title("Distribution of Activity Scores")
plt.xlabel("Activity Score")
plt.ylabel("Number of Students")

plt.show()


# -------------------------------
# 4. Scatter Plot
# -------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Student_ID"],
    df["Activity_Score"]
)

plt.title("Student ID vs Activity Score")
plt.xlabel("Student ID")
plt.ylabel("Activity Score")

plt.show()


# -------------------------------
# 5. Box Plot
# -------------------------------

plt.figure(figsize=(7, 5))

plt.boxplot(
    df["Activity_Score"],
    vert=True
)

plt.title("Activity Score Distribution")
plt.ylabel("Activity Score")

plt.show()