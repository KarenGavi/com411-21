# Ask user for the first number
print("Please enter the first whole number")
first_number = int(input())

# Ask user for the second number
print("Please enter the whole number")
second_number = int(input())

# Ask the user for the third number
print("Please enter the third whole number")
third_number = int(input())

even_numbers = 0
odd_numbers = 0

# Calculate the number of even numbers and odd numbers entered.
if first_number % 2 == 0:
    even_numbers += 1
else:
    odd_numbers += 1

if second_number % 2 == 0:
    even_numbers += 1
else:
    odd_numbers += 1

if third_number % 2 == 0:
    even_numbers += 1
else:
    odd_numbers += 1
# Display result
print(f"There were {even_numbers} even and {odd_numbers} odd numbers")