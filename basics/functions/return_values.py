# Define first function
def sum_weights(beep_weight, bop_weight):
    total_weight = beep_weight + bop_weight
    return total_weight
# define second function
def calc_avg_weight(beep_weight, bop_weight):
    avg_weight = sum_weights(beep_weight, bop_weight) /2
    return avg_weight

# Define third function
def run():
    print("What is the weight Beep?")
    beep_weight = float(input())

    print("What is the weight Bop?")
    bop_weight = float(input())

    print("What would you like to calculate (sum or average)?")
    action = input()

    # Determine and carry out action
    if action == "sum":
        answer = sum_weights(beep_weight, bop_weight)
        print(f"the sum of Beep's and Bob's weight is {answer:.2f}")
    elif action == "average":
        answer = calc_avg_weight(beep_weight, bop_weight)
        print(f"the average of Beep's and Bop's weight is {answer:.2f}")
    else:
        print("I am not sure what you would like to do.")

# Call to function
run()
