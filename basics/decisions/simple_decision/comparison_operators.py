# Ask user for first number
print("Please enter the first number.")
first_number = int(input())

# Ask user for the second number
print("Please enter the second number")
second_number = int(input())

# Display relevant messaqe
if first_number > second_number:
    print ("The first number is bigger")

elif first_number < second_number:
    print("the second number is bigger")

else:
    print ("Both are equal!")
