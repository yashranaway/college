import numpy as np

# Create an array
data = np.array([10, 20, 30, 40, 50, 60])

# Basic statistical measures
mean_val = np.mean(data)
median_val = np.median(data)
std_dev = np.std(data)
variance = np.var(data)

# Advanced statistical methods
percentile_25 = np.percentile(data, 25)
percentile_90 = np.percentile(data, 90)

# Create another array for correlation
data2 = np.array([15, 25, 35, 45, 55, 65])
correlation_coeff = np.corrcoef(data, data2)

print("Data:", data)
print("\nMean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_dev)
print("Variance:", variance)
print("\n25th Percentile:", percentile_25)
print("90th Percentile:", percentile_90)
print("\nCorrelation Coefficient Matrix:\n", correlation_coeff)



