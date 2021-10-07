
# Ask user to enter number of lives
print("Please enter the number of lives.")
lives = int(input())

# Ask energy level.
print("Please enter energy levels")
energy_level = int(input())

# Ask user the level of shield
print("Please enter the shield level.")
shield = int(input())

# Displays all the health data
print("Health has been set.")
print(f"Lives:  {'♥' * lives}")
print(f"Energy:  {'♥' * energy_level}")
print(f"Shield:  {'♥' * shield}")