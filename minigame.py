import random

num = random.randint(1, 10)
tries = 0

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    tries += 1

    if guess == num:
        print(f"You are right! Number is {num}. You guessed it in {tries} tries.")
        break
    elif num < guess:
        print("Go a little lower.")
    elif num > guess:
        print("Go a little higher.")