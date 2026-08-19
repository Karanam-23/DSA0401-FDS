import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Sample data for 18 adults
data = {
    "Age": [23, 25, 28, 30, 32, 35, 38, 40, 42,
            45, 48, 50, 52, 55, 58, 60, 62, 65],
    "Body_Fat": [12, 15, 18, 20, 22, 24, 25, 27, 29,
                 30, 32, 34, 35, 37, 39, 40, 42, 44]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display Data
print("Hospital Data")
print(df)

# Mean
print("\nMean")
print(df.mean())

# Median
print("\nMedian")
print(df.median())

# Standard Deviation
print("\nStandard Deviation")
print(df.std())

# Boxplots
plt.figure(figsize=(8,4))
plt.boxplot(df["Age"])
plt.title("Boxplot of Age")
plt.ylabel("Age")
plt.show()

plt.figure(figsize=(8,4))
plt.boxplot(df["Body_Fat"])
plt.title("Boxplot of Body Fat %")
plt.ylabel("Body Fat (%)")
plt.show()

# Scatter Plot
plt.figure(figsize=(6,4))
plt.scatter(df["Age"], df["Body_Fat"])
plt.title("Scatter Plot of Age vs Body Fat")
plt.xlabel("Age")
plt.ylabel("Body Fat (%)")
plt.grid(True)
plt.show()

# Q-Q Plot for Age
plt.figure(figsize=(6,4))
stats.probplot(df["Age"], dist="norm", plot=plt)
plt.title("Q-Q Plot of Age")
plt.show()

# Q-Q Plot for Body Fat
plt.figure(figsize=(6,4))
stats.probplot(df["Body_Fat"], dist="norm", plot=plt)
plt.title("Q-Q Plot of Body Fat")
plt.show()
