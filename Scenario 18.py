import pandas as pd

# Create a DataFrame containing post likes
user_data = pd.DataFrame({
    "Post_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Likes": [120, 150, 120, 200, 180, 150, 120, 250, 180, 150]
})

# Display the DataFrame
print("User Interaction Data")
print(user_data)

# Calculate the frequency distribution of likes
likes_frequency = user_data["Likes"].value_counts().sort_index()

# Display the frequency distribution
print("\nFrequency Distribution of Likes")
print(likes_frequency)
