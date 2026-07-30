import numpy as np
import matplotlib.pyplot as plt

# Study time (hours) and Exam scores
study_time = [1, 2, 3, 4, 5, 6, 7, 8]
exam_scores = [40, 50, 55, 65, 70, 80, 85, 95]

# Calculate correlation coefficient
correlation = np.corrcoef(study_time, exam_scores)[0, 1]

print("Correlation Coefficient:", correlation)

# Scatter Plot
plt.figure(figsize=(6, 4))
plt.scatter(study_time, exam_scores, color='blue', s=80)
plt.title("Study Time vs Exam Scores (Scatter Plot)")
plt.xlabel("Study Time (Hours)")
plt.ylabel("Exam Score")
plt.grid(True)
plt.show()

# Line Plot
plt.figure(figsize=(6, 4))
plt.plot(study_time, exam_scores, marker='o', color='green')
plt.title("Study Time vs Exam Scores (Line Plot)")
plt.xlabel("Study Time (Hours)")
plt.ylabel("Exam Score")
plt.grid(True)
plt.show()

# Interpretation
if correlation > 0:
    print("Positive correlation: As study time increases, exam scores increase.")
elif correlation < 0:
    print("Negative correlation: As study time increases, exam scores decrease.")
else:
    print("No correlation between study time and exam scores.")
