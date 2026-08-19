import numpy as np
from scipy import stats

# Blood pressure reduction data
drug = [15, 18, 12, 20, 17, 14, 16, 19, 13, 15,
        21, 16, 18, 14, 17, 20, 15, 13, 19, 16,
        18, 17, 14, 20, 16, 15]

placebo = [8, 10, 7, 12, 9, 11, 8, 10, 6, 9,
           11, 8, 7, 10, 9, 12, 8, 11, 7, 9,
           10, 8, 9, 11, 7]

# Function to calculate 95% confidence interval
def confidence_interval(data):
    n = len(data)
    mean = np.mean(data)
    std = np.std(data, ddof=1)

    t_value = stats.t.ppf(0.975, df=n-1)

    margin_error = t_value * (std / np.sqrt(n))

    lower = mean - margin_error
    upper = mean + margin_error

    return mean, lower, upper

# Drug group
drug_mean, drug_lower, drug_upper = confidence_interval(drug)

# Placebo group
placebo_mean, placebo_lower, placebo_upper = confidence_interval(placebo)

# Display results
print("New Drug Group:")
print("Mean reduction =", round(drug_mean, 2))
print("95% Confidence Interval =",
      (round(drug_lower, 2), round(drug_upper, 2)))

print("\nPlacebo Group:")
print("Mean reduction =", round(placebo_mean, 2))
print("95% Confidence Interval =",
      (round(placebo_lower, 2), round(placebo_upper, 2)))
