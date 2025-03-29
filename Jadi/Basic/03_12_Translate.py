number = int(input())
mydict = {}

for i in range(number):
    x, y = input().split()
    mydict[x] = y

userinput = input().split()
for i in range(len(userinput)):
    if userinput[i] in mydict.keys():
        userinput[i] = mydict[userinput[i]]
    else:
        pass

print(" ".join(userinput))