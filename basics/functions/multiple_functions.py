# Define first function
def display_ladder(steps):
    for steps in range(steps):
        print("|  |")
        print("***")
        print("|  |")

# Define second function
def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    display_ladder(steps)
# Call function
create_ladder()
