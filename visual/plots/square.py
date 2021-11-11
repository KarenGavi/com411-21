import matplotlib.pyplot as plt
# Define first function
def small():
    x = [3,3,4,4,3]
    y = [3,4,4,3,3]
    plt.plot(x, y, 'r:o')

# Define second function
def medium():
    x = [2,2,5,5,2]
    y = [2,5,5,2,2]
    plt.plot(x, y, 'g--s')

# define third function
def large():
    x = [1,1,6,6,1]
    y = [1,6,6,1,1]

    plt.plot(x, y, 'b-p')

# Define last function
def run():
    small()
    medium()
    large()
    plt.show()

run()

