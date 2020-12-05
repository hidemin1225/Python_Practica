# Ask a user's favorite color
# Check to see if it is the same as your favourite colour.
# Code it so that the user can enter in either upper case or lower case.
# Outputs ‘That’s my favourite colour too’ if it’s also your favourite colour.
# If it isn’t, give a different message.

color = input("What is your favorite color?")
print()

if color.lower() == "pink":
    print("That's my favorite color too!")

else:
    print("We seem to have different tastes...")
