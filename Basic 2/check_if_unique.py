'''
Function that checks if a given list of numbers is unique
'''

import random

def is_array_unique(numbers):
    tmp = []
    for i in range(len(numbers)):
        if numbers[i] in tmp:
            return False
        else:
            tmp.append(numbers[i])
    return True

numbers = []

for i in range(3000000):
    num = random.randint(1,100)
    numbers.append(num)
    
print(is_array_unique(numbers))