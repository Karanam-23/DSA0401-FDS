import matplotlib.pyplot as plt

# Monthly data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

temperature = [22, 24, 28, 32, 35, 33, 30, 29, 28, 26, 24, 22]

rainfall = [15, 20, 35, 60, 120, 180, 220, 200, 160, 90, 40, 20]

# 1. Line Plot for Monthly Temperature
plt.figure(figsize=(7, 4))
plt.plot(months, temperature, marker='o', color='blue', linewidth=2)
plt.title("Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

# 2. Scatter Plot for Monthly Rainfall
plt.figure(figsize=(7, 4))
plt.scatter(months, rainfall, color='green', s=80)
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.grid(True)
plt.show()
