# Ask user about charging
print("how many bars should be charged?")
bars = int(input())

# Track number of bars
bars_charged = 0

# Bars charged
print()
while bars_charged < bars:
    bars_charged = bars_charged +1
    print(f"Charging:{'█' * bars_charged }")
print("the battery is fully charged.")