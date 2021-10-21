# define first function
def display_chars(file_path , num_of_chars):
    with open(file_path) as file:
        data = file.read(num_of_chars)
        print(data)
# Define second function
def display_line(file_path):
    with open(file_path) as file:
        data = file.readline().strip()
        print(data)

# Define third function
def display_text(file_path):
    with open(file_path) as file:
        data = file.read()
        print(data)

# Define fourth function
def run():
    display_chars("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")

if __name__ == "__main__":
    run()