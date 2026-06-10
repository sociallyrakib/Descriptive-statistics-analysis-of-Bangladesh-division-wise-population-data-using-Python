# Bangladesh Division Population Analysis
# Data Source: Bangladesh Bureau of Statistics (BBS), Census 2022

divisions = ["Dhaka", "Chittagong", "Rajshahi", "Khulna", 
             "Barisal", "Sylhet", "Rangpur", "Mymensingh"]

population = [44215107, 33202326, 20353119, 17416645, 
              9100102, 11034952, 17610955, 12225498]

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
print("Data Source: BBS Census 2022")
print("Mean Population:    ", round(mean))
print("Median Population:  ", round(median))
print("Std Deviation:      ", round(sd))
print("Most Populated:     ", divisions[population.index(maximum)])
print("Least Populated:    ", divisions[population.index(minimum)])
