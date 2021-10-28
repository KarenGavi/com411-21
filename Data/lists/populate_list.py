# Define the first function
def directions():
    directions = ["move forward", "move backward", "turn left", "turn right"]
    return directions
# Define second function
def menu():
    print("please select a direction")
    dirs = directions()
    for index in range(len(dirs)):
        print(f"{index}: {dirs[index]}")
    index = int(input())
    return dirs[index]
# Define third function
def run():
    route = []
    print("Working out escape route..")
    for count in range(5):
        route.append(menu())
    print(f"escape route:{route}")

if __name__ == "__main__":
    run()