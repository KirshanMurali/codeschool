import random

def lotto_numbers():
    lotto_nums = []
    for i in range(5):
        lotto_nums.append(random.randint(1, 53)) 
        
    return lotto_nums

numbers=1,2,3,4,5,6,7,8,9,10
lotto_numbers(numbers)
print(numbers)