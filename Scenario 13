import pandas as pd

# Stock closing prices
stock_data = {
    "Day": [1, 2, 3, 4, 5, 6, 7],
    "Closing_Price": [150, 155, 148, 160, 158, 162, 157]
}

# Create DataFrame
df = pd.DataFrame(stock_data)

# Display stock data
print("Stock Data")
print(df)

# Calculate average closing price
average_price = df["Closing_Price"].mean()

# Calculate variability (Standard Deviation)
variability = df["Closing_Price"].std()

# Display results
print("\nAverage Closing Price:", average_price)
print("Variability (Standard Deviation):", variability)

# Insight
if variability > 5:
    print("Insight: Stock prices show high variability.")
else:
    print("Insight: Stock prices show low variability.")
