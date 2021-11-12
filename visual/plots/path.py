import matplotlib.pyplot as plt

# Define first function
def coordinate():
    print("PLease enter an x value:")
    x = int(input())

    print("Please enter a y value:")
    y = int(input())

    return (x, y)

# Define second function
def path():
    print("Retrieve path...")
    x_values = []
    y_values = []

    for count in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])
    return [x_values, y_values]

# Define third function
def run():
    values = path()
    plt.plot(values[0], values[1], "r--o")
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.show()


run()
