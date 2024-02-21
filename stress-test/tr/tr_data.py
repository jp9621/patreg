import numpy as np
import random

def filler(pattern):
    new_pattern = [pattern[0]]  # Start with the first element (validity)
    num_fillers = 2
    for i in range(1, len(pattern) - 1):
        new_pattern.append(pattern[i])  # Add the original data point
        # Generate filler values between the current data point and the next one
        for _ in range(num_fillers):
            filler_val = random.uniform(pattern[i], pattern[i+1])
            new_pattern.append(filler_val)
    new_pattern.append(pattern[-1])  # Add the last element
    return new_pattern




def generate_pattern(validity):
    if validity:
        p1 = random.uniform(0, 100)
        p2 = random.uniform(0, p1)
        p3 = random.uniform(p2, p1)
        p4 = random.uniform(p2, p3)
        return [validity, p1, p2, p3, p4]
    if not validity:
        pattern = [validity, random.uniform(0,100), random.uniform(0,100), random.uniform(0,100), random.uniform(0,100)]
        if pattern[1] > pattern[2] and pattern[2] < pattern[3] and pattern[4] < pattern [3] and pattern[3] < pattern[1] and pattern[4] > pattern[2]:
            pattern.remove(pattern[0])
            pattern.insert(0, True)
        return pattern

num_patterns = 100000
patterns = []
for _ in range(num_patterns):
    patterns.append(filler(generate_pattern(True)))

for _ in range(num_patterns):
    patterns.append(filler(generate_pattern(False))) 



patterns_array = np.array(patterns)



np.savetxt('stress-test/tr/tr_data.csv', patterns_array, delimiter=',', fmt='%.5f')

