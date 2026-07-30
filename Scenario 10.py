import matplotlib.pyplot as plt

# Monthly sales data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [25000, 30000, 28000, 35000, 40000, 38000]

# Line Plot
plt.figure(figsize=(6, 4))
plt.plot(months, sales, marker='o', color='blue')
plt.title("Monthly Sales - Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# Bar Plot
plt.figure(figsize=(6, 4))
plt.bar(months, sales, color='green')
plt.title("Monthly Sales - Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
