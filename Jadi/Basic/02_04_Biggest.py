mylist = []
age = 0

while age != -1:
    age = int(input())
    mylist.append(age)

mylist.sort()
print(mylist[-1])