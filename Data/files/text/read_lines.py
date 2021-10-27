# Define first function
def search(file_path):
    print("Searching...")
    w open(file_path) as file:
        for location in file:
            print(f"Looked in {location.strip()}")
        print("...done!")

if __name__ == "__main__":
    run()