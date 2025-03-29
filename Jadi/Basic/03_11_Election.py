number = int(input())
mydict = {}

for i in range(number):
    vote = input().lower()
    mydict[vote] = mydict.get(vote, 0) + 1

mylist = list(mydict.items())
mylist.sort()

for i, j in mylist:
    print(i, j)