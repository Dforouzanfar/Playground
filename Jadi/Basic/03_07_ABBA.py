userinput = input()

AB = userinput.find("AB")
BA = userinput.find("BA", AB + 2)
BA2 = userinput.find("BA")
AB2 = userinput.find("AB", BA2 + 2)

if (AB != -1 and BA != -1) or (AB2 != -1 and BA2 != -1):
    print("YES")
else:
    print("NO")
