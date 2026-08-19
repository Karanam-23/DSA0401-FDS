import numpy as np
from scipy.stats import ttest_ind

A = [0.12, 0.15, 0.11, 0.14, 0.13, 0.16, 0.12, 0.15]
B = [0.10, 0.11, 0.09, 0.12, 0.10, 0.13, 0.11, 0.12]

t, p = ttest_ind(A, B)

print("Mean A:", np.mean(A))
print("Mean B:", np.mean(B))
print("p-value:", p)

if p < 0.05:
    print("There is a statistically significant difference")
else:
    print("There is no statistically significant difference")
