mylist = []

for i in range(20):
    counter = 0
    number = int(input())
    for i in range(1, number+1):
        if number % i == 0:
            counter += 1
    mylist.append((number, counter))

mylist.sort(reverse=True)
mylist.sort(key = lambda x: x[1], reverse=True)

print(mylist[0][0], mylist[0][1])