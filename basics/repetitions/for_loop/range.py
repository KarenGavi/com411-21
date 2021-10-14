#Display message to user
print("What level of brightness is required?")

brightness = int(input())
# display message
print("Adjusting brightness...")

for brightness in range(2,brightness + 1, 2 ):
    print(f"Beep's brightness level: {'*' * brightness}")
    print(f"Bop's's brightness level: {'*' * brightness}")

print("Adjustments complete!")




