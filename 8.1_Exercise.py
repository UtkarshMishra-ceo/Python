#number guessing game
import random
num=random.randint(1,100)
for i in range(100):
    n=int(input("guess the number:"))
    if n==num:
        print(f"You guessed correct number ar {i} times")
        break
    else:
        if n>num:
            print("Num is to big")
            continue
        else:
            print("Num is to small")
            continue

    