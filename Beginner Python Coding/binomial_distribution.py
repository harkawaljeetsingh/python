import numpy as np

# Parameters for the binomial distribution
n = 10  # number of trials
p = 0.5  # probability of success in each trial

# Generate a single random number following a binomial distribution
random_number = np.random.binomial(n, p)
print(f"Random number (Binomial): {random_number}")

# Generate an array of random numbers
num_samples = 10
random_numbers = np.random.binomial(n, p, num_samples)
print(f"Array of random numbers (Binomial): {random_numbers}")
