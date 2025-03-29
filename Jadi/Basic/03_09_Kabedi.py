number = int(input())
games = list(map(int, input().split()))
for i in games:
    if i >= 3:
        games.remove(i)

teams = len(games)//3
print(teams)
