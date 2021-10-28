# Define first function
import json
def read(file_path):
    print("Reading...", end="")
    with open(file_path) as file:
        data = json.load(file)
    print("Done!")
    return data
# Define second function
def save(file_path, data):
    print("Eporting..", end="")
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    print("Done!")
# Define third function
def run():
    json_data = read("robocity.json")
    save("exported.json", json_data)
if __name__ == "__main__":
    run()
