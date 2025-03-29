number = int(input())
mylist = []

for _ in range(number):
    x, y = map(int, input().split())
    mylist.append((x, y))

mylist.sort()

for i in range(1, len(mylist)):
    if mylist[i-1][1] > mylist[i][1]:
        print("happy irsa")
        break

else:
    print("poor irsa")
