number = int(input())
counter = 0

for i in range(2, number):
    if number % i == 0:
        counter += 1

if counter > 0:
    print("not prime")
else:
    print("prime")