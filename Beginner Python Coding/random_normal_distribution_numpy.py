import numpy as np

# Parameters for the normal distribution
mean = 0
std_dev = 1

# Generate a single random number
random_number = np.random.normal(mean, std_dev)
print(f"Random number (NumPy): {random_number}")

# Generate an array of random numbers
num_samples = 10
random_numbers = np.random.normal(mean, std_dev, num_samples)
print(f"Array of random numbers (NumPy): {random_numbers}")
