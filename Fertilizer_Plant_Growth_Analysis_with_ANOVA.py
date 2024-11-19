# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Step 1: Define Data
# Plant growth data for three fertilizers
fertilizer_A = [20, 22, 23, 21, 24]
fertilizer_B = [30, 28, 31, 29, 27]
fertilizer_C = [25, 26, 27, 24, 23]

# Combine the data into a DataFrame for visualization and analysis
data = {
    "Fertilizer": ["A"] * len(fertilizer_A) + ["B"] * len(fertilizer_B) + ["C"] * len(fertilizer_C),
    "Plant Growth": fertilizer_A + fertilizer_B + fertilizer_C
}
df = pd.DataFrame(data)

# Step 2: Visualize the Data
plt.figure(figsize=(8, 6))
plt.boxplot([fertilizer_A, fertilizer_B, fertilizer_C], labels=["Fertilizer A", "Fertilizer B", "Fertilizer C"])
plt.title("Plant Growth Distribution by Fertilizer")
plt.ylabel("Plant Growth (cm)")
plt.xlabel("Fertilizer Type")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Step 3: Perform One-Way ANOVA
f_statistic, p_value = stats.f_oneway(fertilizer_A, fertilizer_B, fertilizer_C)

# Output the ANOVA results
print(f"F-statistic: {f_statistic:.2f}")
print(f"P-value: {p_value:.4f}")

# Step 4: Set Significance Level and Interpret Results
alpha = 0.05  # 5% significance level
num_groups = 3  # Number of fertilizers
num_observations = len(fertilizer_A) + len(fertilizer_B) + len(fertilizer_C)
df_between = num_groups - 1  # Degrees of freedom for groups
df_within = num_observations - num_groups  # Degrees of freedom within groups

# Calculate the F-critical value
f_critical_value = stats.f.ppf(1 - alpha, df_between, df_within)

print(f"F-critical value: {f_critical_value:.2f}")

if f_statistic > f_critical_value:
    print("Result: Reject the null hypothesis.")
    print("There is a significant difference in plant growth among the fertilizers.")
else:
    print("Result: Fail to reject the null hypothesis.")
    print("There is no significant difference in plant growth among the fertilizers.")

# Step 5: Summary Table
summary = pd.DataFrame({
    "Fertilizer": ["A", "B", "C"],
    "Mean Growth": [np.mean(fertilizer_A), np.mean(fertilizer_B), np.mean(fertilizer_C)],
    "Std Dev Growth": [np.std(fertilizer_A, ddof=1), np.std(fertilizer_B, ddof=1), np.std(fertilizer_C, ddof=1)]
})
print("\nSummary Statistics:")
print(summary)
