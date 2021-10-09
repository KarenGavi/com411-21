# Ask question on type of adventure
print("what type of adventure should i have?")
adventure_type = input()

# Choosing type of adventure
if (adventure_type == "short") or (adventure_type == "scary"):
    print("Entering the dark forest!")
elif (adventure_type == "safe") or (adventure_type == "long"):
    print("taking the safe route!")
else:
    print("not sure which route to take")