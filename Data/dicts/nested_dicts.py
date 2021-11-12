# Define first function
def short_pattern():
    pattern = {"Sequence":"101", "Occurrences":5}
    return pattern

# Define second function
def medium_pattern():
    pattern = {"Sequence":"111000", "Occurrences":25}
    return pattern

# Define third function
def long_pattern():
    pattern = {"Sequence":"1100110011001100", "Occurrences":50}
    return pattern

# Define fourth function
def run():
    print("Analysing patterns...")
    patterns = {"short sequence":short_pattern(),
                "medium sequence":medium_pattern(),
                "long sequence":long_pattern()
                }

    for key, value in patterns.items():
        print(f"{key}: {value}")

run()