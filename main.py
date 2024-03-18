"""
This program calculates prices for custom house signs.
"""


# Declare and initialize variables here.
charge = 0.00
numChars = 8
color = "gold"
woodType = "oak"

# Charge for this sign.
charge = 35.00

# Number of characters.
numChars = int(input("Please enter the number of sign characters: "))

# Color of characters.
color = input("Is your lettering black, white, or gold?: ")

# Type of wood.
woodType = input("Is the sign oak or pine?: ")

# Write assignment and if statements here as appropriate.
if numChars > 5:
  charge += (numChars - 5) * 4.00

if color == "gold":
  charge += 15.00

if woodType == "oak":
  charge += 20.00

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
