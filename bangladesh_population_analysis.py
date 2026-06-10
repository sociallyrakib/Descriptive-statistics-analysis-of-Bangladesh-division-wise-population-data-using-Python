# Bangladesh Division Population Analysis
# Data Source: Bangladesh Bureau of Statistics

divisions = ["Dhaka", "Chittagong", "Rajshahi", "Khulna", 
             "Barisal", "Sylhet", "Rangpur", "Mymensingh"]

population = [36054418, 28423019, 18484858, 15563000, 
              8325666, 9910219, 15665000, 11370000]

# Basic calculations
n = len(population)
mean = sum(population) / n
sorted_pop = sorted(population)

if n % 2 == 0:
    median = (sorted_pop[n//2 - 1] + sorted_pop[n//2]) / 2
else:
    median = sorted_pop[n//2]

minimum = min(population)
maximum = max(population)

variance = sum((p - mean)**2 for p in population) / n
sd = variance ** 0.5

# Results
print("=== Bangladesh Division Population Analysis ===")
print("Mean Population:    ", round(mean))
print("Median Population:  ", round(median))
print("Std Deviation:      ", round(sd))
print("Most Populated:     ", divisions[population.index(maximum)])
print("Least Populated:    ", divisions[population.index(minimum)])
