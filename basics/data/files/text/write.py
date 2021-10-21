# Define first function
def search(file_path):
    print("Searching...")

    sections =""
    books ="Books:\n"

    with open(file_path) as file:
        for line in file:
            if line.startswith("Section"):
                sections += line
            else:
                books += line

    print("Done!")

    return f"{sections}\n\n{books}"

# Define second function
def save(file_path, data):
    print("Saving..")
    with open(file_path, "w") as file:
        file.write(data)
    print("Done!")

# define third function
def run():
    # Call the functions
    data = search("books.txt")
    save("exported_books.txt", data)


if __name__ == "__main__":
    run()