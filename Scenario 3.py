"""You are working on a project that involves analyzing a dataset containing information
about houses in a neighborhood. The dataset is stored in a CSV file, and you have imported it into a
NumPy array named house_data. Each row of the array represents a house, and the columns contain
various features such as the number of bedrooms, square footage, and sale price.
Question: Using NumPy arrays and operations, how would you find the average sale price of houses
with more than four bedrooms in the neighborhood?"""

import numpy as np

# Columns:
# [Bedrooms, Square Footage, Sale Price]
house_data = np.array([
    [3, 1500, 250000],
    [5, 2200, 450000],
    [4, 1800, 320000],
    [6, 3000, 600000],
    [5, 2500, 500000]
])

# Select houses with more than 4 bedrooms
filtered_houses = house_data[house_data[:, 0] > 4]

# Calculate the average sale price
average_sale_price = np.mean(filtered_houses[:, 2])

print("Average Sale Price:", average_sale_price)
