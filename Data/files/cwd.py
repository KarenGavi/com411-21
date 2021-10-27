import os

#Define first function
def cwd():
    path = os.getcwd()
    print(f"Current working directory: {path}")
    print(f"The directory contains the following files:")

    for file in os.listdir(path):
        print(file)

# Define second function
def run():
    print("Proccessing...")

# Call first function
cwd()

if __name__ == "__main__":
  run()