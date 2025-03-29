vowels = ["a", "e", "o", "u", "i"]
output = ""
userinput = input()

for i in userinput.lower():
    if i not in vowels:
        output += (f".{i}")
    else:
        pass

print(output)