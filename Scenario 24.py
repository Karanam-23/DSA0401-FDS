import pandas as pd
import numpy as np
from scipy.stats import norm

data = pd.read_csv("rare_elements.csv")

n = int(input("Enter sample size: "))
confidence = float(input("Enter confidence level: "))
precision = float(input("Enter desired precision: "))

sample = data.iloc[:n, 0]

mean = np.mean(sample)
std = np.std(sample, ddof=1)

z = norm.ppf((1 + confidence) / 2)
margin = z * std / np.sqrt(n)

print("Sample Mean:", mean)
print("Confidence Interval:", mean - margin, "to", mean + margin)

if margin <= precision:
    print("Desired precision achieved")
else:
    print("Desired precision not achieved")
