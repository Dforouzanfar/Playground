userinput = input()
userlist = userinput.split("+")
mylist = [int(num) for num in userlist]
mylist.sort(reverse=True)
output = "+".join(map(str, mylist))
print(output)