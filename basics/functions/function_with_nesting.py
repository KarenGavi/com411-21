# Ask user to enter a word
def identify():
    print("What lies before us?")
    visual = input()
# Display message
    if visual == "a large boulder":
        print("it's time to run!")
    else:
        print("We will be fine.")

# Call the function
identify()