import numpy as np
import random

def filler(pattern):
    new_pattern = [pattern[0]] 
    num_fillers = 2
    for i in range(1, len(pattern) - 1):
        new_pattern.append(pattern[i])  
        
        for _ in range(num_fillers):
            filler_val = random.uniform(pattern[i], pattern[i+1])
            new_pattern.append(filler_val)
    new_pattern.append(pattern[-1])
    return new_pattern



def upFiller(pattern, upperLimit):
    new_pattern = []
    
    for i in range(len(pattern) - 1):
        start_val = pattern[i]
        new_pattern.append(start_val)
        end_val = pattern[i + 1]
        num_fillers = 1
        
        for _ in range(num_fillers):
            filler_val = random.uniform(start_val, upperLimit)
            new_pattern.append(filler_val)
        
    return new_pattern

def generate_pattern(validity):
    if validity:
        p1 = random.uniform(0, 100)
        p2 = random.uniform(0, p1)
        p3 = random.gauss(p2, 5) 
        p4 = random.gauss(p2, 5)
        p3 = min(max(0, p3), p1)
        p4 = min(max(0, p4), p1)
        pattern1 = [validity, p1, p2]
        pattern2 = upFiller([p3,p4], p1)
        final_pattern = filler(pattern1 + pattern2)
        return final_pattern
    
    if not validity:
        final_pattern = [validity]
        for _ in range(10):
            final_pattern.append(random.uniform(0,100))
        return final_pattern



num_patterns = 100000
patterns = []
for _ in range(num_patterns):
    patterns.append(generate_pattern(True))

for _ in range(num_patterns):
    patterns.append(generate_pattern(False))


patterns_array = np.array(patterns)

np.savetxt('st/st_data.csv', patterns_array, delimiter=',', fmt='%.5f')
