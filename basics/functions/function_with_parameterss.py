# Define function
def climb_ladder(steps_remaining, steps_crossed):
    # Compare values
    if steps_remaining > steps_crossed:
        print("Still some way to go!")
    else:
        print("we almost there!")
# Call the function
climb_ladder(5, 2)

climb_ladder(2, 5)

