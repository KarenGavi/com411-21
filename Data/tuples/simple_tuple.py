# Define first function
def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)
# Define second function
def run():
# Call first function
    print(f"minimum likelihood of falling: {likelihood()}%")
if __name__ == "__main__":
    run()