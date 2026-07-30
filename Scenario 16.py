# Sample text
text = """
Data Science is an interdisciplinary field.
Data Science uses scientific methods to analyze data.
Data analysis helps in making better decisions.
"""

# Convert text to lowercase
text = text.lower()

# Remove punctuation
text = text.replace(".", "")
text = text.replace(",", "")

# Split text into words
words = text.split()

# Create dictionary to store word frequency
frequency = {}

# Count frequency of each word
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Display frequency distribution
print("Word Frequency Distribution\n")

for word, count in frequency.items():
    print(word, ":", count)
