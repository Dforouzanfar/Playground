userinput = input().lower()

h = userinput.find("h")
e = userinput.find("e", h+1)
l = userinput.find("l", e+1)
l2 = userinput.find("l", l+1)
o = userinput.find("o", l2+1)

indices = [h, e, l, l2, o]

if all(index != -1 for index in indices):
    print("YES")
else:
    print("NO")