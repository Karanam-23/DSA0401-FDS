import matplotlib.pyplot as plt
import numpy as np

# Sample Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = np.random.randint(100, 500, size=12) # Random sales data for 12 months

# --- 1. Line Plot of monthly sales over time ---
plt.figure(figsize=(10, 5))
plt.plot(months, sales, marker='o', linestyle='-', color='b')
plt.title('Monthly Sales Trend (Line Plot)')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

# --- 2. Scatter Plot of monthly sales distribution ---
plt.figure(figsize=(10, 5))
plt.scatter(months, sales, color='r', marker='x')
plt.title('Monthly Sales Distribution (Scatter Plot)')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

# --- 3. Bar Plot of monthly sales data ---
plt.figure(figsize=(10, 5))
plt.bar(months, sales, color='g')
plt.title('Monthly Sales Overview (Bar Plot)')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(axis='y')
plt.show()
