# Define first function
def directions():
    directions = ["move forward", "move backward", "turn left", "turn right"]
    return directions
# Define second function
def run():
    print(directions())

if __name__ == "__main__":
    run()