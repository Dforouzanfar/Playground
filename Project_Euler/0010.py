import math

def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(num) + 1), 2):
        if num % i == 0:
            return False
    return True

total = 0
for j in range(2, 2000000):
    if is_prime(j):
        total += j

print(total)