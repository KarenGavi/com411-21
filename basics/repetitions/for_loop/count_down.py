# Display message to user
print("how far are we from the cave?")
distance = int(input())

for distance in range(distance, 0, -1):
    print(f"{distance} steps remaining")

print("we have reached the cave!")