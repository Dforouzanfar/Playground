import random

lower_bound, upper_bound = 1, 99

while True:
    
    guess = random.randint(lower_bound, upper_bound)
    print(guess)
    outcome = input()
    
    if outcome == "k":
        upper_bound = int(guess) - 1
    elif outcome == "b":
        lower_bound = int(guess) + 1
    elif outcome == "d":
        break
    else:
        raise KeyError