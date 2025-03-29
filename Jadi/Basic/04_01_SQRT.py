from math import sqrt, floor

number = int(input())
mylist = []

for i in range(number):
    userinput = int(input())
    x = floor(sqrt(userinput) * 10000) / 10000
    mylist.append(x)

for i in mylist:
    print(f"{i:.4f}")
