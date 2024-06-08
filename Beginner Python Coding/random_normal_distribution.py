import random

# Parameters for the normal distribution
mean = 0
std_dev = 1

# Generate a random number following a normal distribution
random_number = random.gauss(mean, std_dev)
print(f"Random number (gauss): {random_number}")

# Generate another random number using normalvariate
random_number2 = random.normalvariate(mean, std_dev)
print(f"Random number (normalvariate): {random_number2}")
