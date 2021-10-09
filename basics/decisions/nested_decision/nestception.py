# Ask user a question
print("where should I look?")
user_response = input()

if user_response == "in the bedroom":
    print("where in the bedroom should i look?")

    in_bedroom = input()

    if in_bedroom == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("found a mess but no battery")

# Check bathroom

elif user_response == "in the bathroom":
    print("Where in the bathroom should i look?")
    in_bathroom = input()

    if in_bathroom == "in the bathtub":
        print("Found a rubber duck but no battery")

    else:
        print("Found a wet surface but no battery")

# Check the lab

elif user_response == "in the lab":
    print("where in the lab should i look?")
    in_lab = input()

    if in_lab == "on the table":
        print("Yes! I found the battery!")
    else:
        print("Found some tool but no battery")

else:
    print("i don not know where that is but i will keep looking")
