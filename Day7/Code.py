import numpy as np

# Generate 100 random numbers from a normal distribution
data = np.random.normal(loc=0, scale=1, size=100)

# Calculate mean and standard deviation
mean_value = np.mean(data)
std_value = np.std(data)

print("Generated Data:\n", data)
print("\nMean:", mean_value)
print("Standard Deviation:", std_value)

