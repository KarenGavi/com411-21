# Define first function
def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods), max(likelihoods)

# Define second function
def run():
    probabilities = likelihood()
    print(f"minimum likelihood of falling: {probabilities[0]}%")
    print(f"maximum likelihood of falling: {probabilities[1]}%")
if __name__ == "__main__":
    run()

