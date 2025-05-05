import random

traps = random.sample(range(1, 101), 3)
counter = 1

while counter <= 100:
    input("Press Enter to continue the game ")
    if counter in traps:
        print(f"You stepped on a trap at step {counter}! Game over.")
        break
    print(f"{counter} is safe. Go ahead!")
    counter += 1

if counter > 100:
    print("Congratulations! You've reached the end without stepping on any traps!")
print(f"Traps were in {traps}")