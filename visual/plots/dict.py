import matplotlib.pyplot as plt
import random as rnd

# Define first function
def data():
    paths = {}

    print("What type of line (:, -- or -)")
    line_style = input()

    print("what style colour would you want to use (r, g or b)")
    colour_style = input()

    print("what style marker would you like (o, s or ^) ")
    marker_style = input()

    paths['line_style'] = line_style
    paths['colour_style'] = colour_style
    paths['marker_style'] = marker_style

    return paths
# Define second function
def generate():
    print("How many lines would you like to display?")
    num_lines = int(input())

    for num_line in range(num_lines):
        values = data()
        x = rnd.sample(range(1, 10), 5)
        y = rnd.sample(range(1, 10), 5)
        format = f"{values['colour_style']}{values['line_style']}{values['marker_style']}"
        plt.plot(x, y, format)

    plt.show()

    def run():
        print("Running...")
        generate()
        print("Done!")

    run()

