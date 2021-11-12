def pattern():
    sequences = {}
    sequences["Short sequence"] = 3
    sequences["Medium sequence"] = 2
    sequences["Long sequence"] = 1
    return sequences

# Define first function
def display_keys(data):
    print("Keys:")
    for key in data:
        print(key)
    print()

# Define second function
def display_values(data):
    print("Values:")
    for value in data.values():
        print(value)
    print()

# Define third funtion
def display_items(data):
    print("Pairs:")
    for key, value in data:
        print(f"{key}; {value}")
        print()
# Define final function
def run():
    data = pattern()
    print(f"Dictionary:\n {data}")
    display_keys(data)
    display_values(data)
    display_items(data)

run()
