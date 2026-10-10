import random
num = random.randint(1, 100)
guess = None
while guess != num:
    guess = int(input("Enter your guess (1-100): "))
    if guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high!")
print("Correct! The number was", num)
