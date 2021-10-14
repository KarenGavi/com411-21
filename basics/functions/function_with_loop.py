# define function
def cross_bridge(steps):
    for step in range(steps):
        print("Crossed step.")
    if steps > 5:
            print("The bridge is collapsing!")
    else:
            print("we must keep going!")

# Call function
cross_bridge(3)
cross_bridge(6)
