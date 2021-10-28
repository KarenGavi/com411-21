# Define function
def directions():
    directions = ["move forward", "move backward", "turn left", "turn right"]
    return directions
# Define second function
def menu():
    print("Please select a direction:")
# Call the first function
dirs = directions()
for index in range(len(dirs)):
    print(f"{index}: {dirs[index]}")

# Define third function
def run():
    menu()

