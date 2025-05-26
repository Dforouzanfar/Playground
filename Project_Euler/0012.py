import math

def count_factors(n):
    count = 0
    for i in range(1, int(math.isqrt(n))+1):
        if n % i == 0:
            count += 2 if i * i != n else 1
    return count

i = total = 0

while True:
    count = count_factors(total)
    if count > 500:
       print(total)
       break
    i += 1
    total += i