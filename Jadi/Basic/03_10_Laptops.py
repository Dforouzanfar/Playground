number = int(input())
mylist = list()

for i in range(number):
    userinput = input().split()
    mylist.append((int(userinput[0]), int(userinput[1])))

mylist.sort()

for i, j in mylist:
