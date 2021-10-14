# Display message
print("Program Started!")

# Display standard character
print("please enter a standard character")
character = input()

if len(character) ==1:
    print(f"the ASCII code for {character} is {ord(character)}")
else:
    print("A single character was expected.")

print("Program ended")