import pandas as pd

# Create a DataFrame with customer ages
sales_data = pd.DataFrame({
    "Customer_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Age": [22, 25, 22, 30, 25, 28, 22, 35, 30, 25]
})

# Display the DataFrame
print("Customer Sales Data")
print(sales_data)

# Calculate frequency distribution of ages
age_frequency = sales_data["Age"].value_counts().sort_index()

# Display the frequency distribution
print("\nFrequency Distribution of Customer Ages")
print(age_frequency)
