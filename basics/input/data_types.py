# Ask question to user about their name
print("What is your name human?")
name = input()

# Ask question about the age of the user
print("How old are you?")
age = int(input())

# Ask question about the users height
print("How tall are you?")
height = float(input())

# Ask question about the weight of user
print("How much do you weight?")
weight = float(input())

# Calculate bmi
bmi = weight / (height ** 2)

#Display all information of the user in a sentence.
print(f"{name} you are {age} years old and your bmi is {bmi}")

