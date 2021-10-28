# Define first function
def export(file_path ,num_bots):
    print("Exporting..")
    with open(file_path, "a") as file:
        for count in range(num_bots):
            print("please enter the bot id:")
            bot_id = int(input())

            print ("please enter the name of the bot:")
            bot_name = input()

            print("please enter the paint for the bot:")
            bot_paint = input()
            data = f"{bot_id}, {bot_name}, {bot_paint}\n"
            file.write(data)
    print("Done!")
# Define second function
def run():
    export("exported_bots.csv", 2)

if __name__ == "__main__":
    run()