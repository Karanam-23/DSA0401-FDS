import pandas as pd

# Create a DataFrame containing customer reviews
reviews_data = pd.DataFrame({
    "Review": [
        "Good product and good quality",
        "Excellent product",
        "Good quality and excellent service",
        "Average product",
        "Good service and good support"
    ]
})

# Display the reviews
print("Customer Reviews")
print(reviews_data)

# Combine all reviews into a single string
text = " ".join(reviews_data["Review"])

# Convert text to lowercase
text = text.lower()

# Remove punctuation
text = text.replace(".", "")
text = text.replace(",", "")

# Split the text into words
words = text.split()

# Calculate frequency distribution
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Display the frequency distribution
print("\nFrequency Distribution of Words\n")

for word, count in frequency.items():
    print(word, ":", count)
