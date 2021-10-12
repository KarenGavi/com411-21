# Ask user which cables to avoid
print("how many live cables must I avoid?")
cable_to_avoid = int(input())


# Declare the number of cables to avoid
cables_avoided = 0

# Avoided cables
print()
while cables_avoided < cable_to_avoid:
    print("Avoiding..", end="")
    cables_avoided = cables_avoided + 1
    print (f"done! {cables_avoided } cables avoided.")