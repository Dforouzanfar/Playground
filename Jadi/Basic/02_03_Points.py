total, counter = 0, 0
for i in range(30):
    point = int(input())
    if point == 3:
        counter += 1
    total += point

print(total, counter)