import random
print("Please enter the minimum value:")
min_value = int(input())

print("Please enter the maximum value")
max_value = int(input())

random_number = random.randrange( min_value, max_value)
print(f"I am thinking of a number between {min_value } and {max_value}")
print("Can you guess what is is?")

guessed_correctly = False

while not guessed_correctly:
    print("Please enter a number:")
    guess = int(input())

    if guess == random_number:
        print("Congratulation! You guessed the correct answer!")
        guessed_correctly = True

    elif guess < random_number:
        print("guess higher")
    else:
        print("Guess lower")

print("game over!")