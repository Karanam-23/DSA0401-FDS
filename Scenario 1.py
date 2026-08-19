"""You are working on a project that involves analyzing student performance data for a
class of 32 students. The data is stored in a NumPy array named student_scores, where each row
represents a student and each column represents a different subject. The subjects are arranged in the
following order: Math, Science, English, and History. Your task is to calculate the average score for
each subject and identify the subject with the highest average score.
Question: How would you use NumPy arrays to calculate the average score for each subject and
determine the subject with the highest average score? Assume 4x4 matrix that stores marks of each
student in given order."""
import numpy as np

# Rows = Students
# Columns = Math, Science, English, History
student_scores = np.array([
    [85, 78, 92, 88],
    [90, 82, 85, 91],
    [76, 89, 80, 84],
    [88, 91, 87, 90]
])

# Subject names
subjects = ["Math", "Science", "English", "History"]

# Calculate average score for each subject (column-wise)
average_scores = np.mean(student_scores, axis=0)

# Find the subject with the highest average
highest_index = np.argmax(average_scores)
highest_subject = subjects[highest_index]

# Display results
print("Average Scores:")
for subject, avg in zip(subjects, average_scores):
    print(f"{subject}: {avg:.2f}")

print("\nSubject with Highest Average Score:", highest_subject)
print("Highest Average Score:", average_scores[highest_index])
