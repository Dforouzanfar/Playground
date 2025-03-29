userinput = input()
lowercase = sum(1 for i in userinput if i.islower())
uppercase = len(userinput) - lowercase

if lowercase >= uppercase:
    print(userinput.lower())
else:
    print(userinput.upper())