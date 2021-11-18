import matplotlib.pyplot as plt

# Define first function

def read_data(file_path):
    temps = []
    with open(file_path) as file:
        for line in file:
            temps.append(float(line.strip()))
    return temps

# Define second function
def run():
    data = read_data('temps.txt')
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(range(len(data)), data)
    ax2.plot(range(len(data)), data)
    plt.show()
run()
