import pandas as pd

# Temperature data (°C)
temperature_data = {
    "City": ["Chennai", "Bangalore", "Hyderabad", "Mumbai"],
    "Day1": [35, 28, 32, 30],
    "Day2": [36, 27, 33, 31],
    "Day3": [34, 29, 31, 29],
    "Day4": [37, 28, 34, 32],
    "Day5": [35, 27, 32, 30]
}

# Create DataFrame
df = pd.DataFrame(temperature_data)

print("Temperature Data")
print(df)

# Calculate Mean Temperature
df["Mean_Temperature"] = df.iloc[:, 1:6].mean(axis=1)

# Calculate Standard Deviation
df["Standard_Deviation"] = df.iloc[:, 1:6].std(axis=1)

# Calculate Temperature Range
df["Temperature_Range"] = df.iloc[:, 1:6].max(axis=1) - df.iloc[:, 1:6].min(axis=1)

print("\nMean Temperature of Each City")
print(df[["City", "Mean_Temperature"]])

print("\nStandard Deviation of Each City")
print(df[["City", "Standard_Deviation"]])

# City with Highest Temperature Range
highest_range = df.loc[df["Temperature_Range"].idxmax()]

print("\nCity with Highest Temperature Range")
print(highest_range["City"])
print("Temperature Range:", highest_range["Temperature_Range"])

# City with Most Consistent Temperature
consistent_city = df.loc[df["Standard_Deviation"].idxmin()]

print("\nCity with Most Consistent Temperature")
print(consistent_city["City"])
print("Standard Deviation:", consistent_city["Standard_Deviation"])
