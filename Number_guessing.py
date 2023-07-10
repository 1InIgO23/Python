import random

num = random.randint(0, 10)

score = 10
print("Your score is " + str(score))

def numer_type():
    if num % 2 == 0:
        print("The number is even(par)")
    else:
        print("The number is odd(impar)")

def win_lose(x):
    if x == True:
        print("You won!")
    else:
        print("You lose.")

counter = 10
while True:
    try:
        guess = int(input("Guess the number: "))
        if guess == num:
            y = True
            win_lose(y)
            break
        elif guess < num:
            print("Higher...")
            counter = counter - 1
            score = score - 1
            print("Your score is " + str(score))
        elif guess > num:
            print("Lower...")
            counter = counter - 1
            score = score - 1
            print("Your score is " + str(score)) 
        if score == 0:
            y = False
            win_lose(y)
            break
        elif score == 5:
            numer_type()
    except ValueError:
        print("Invalid input, must be a number.")
