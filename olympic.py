# Ask a user to name one of the Olympic medals (Gold, Silver, Bronze)
# Code it so that the user can use either upper case or lower case.
# If the user’s answer is correct, output ‘Correct‘, else output a different message.

print("Name one of the colors of Olympic medals!")
medal = input()


if medal.lower() in ["gold", "silver", "bronze"]:
    print("Awesome! You are absolutely right!")
else:
    while medal.lower() != ["gold", "silver", "bronze"]:
        print("Are you sure? Try again?")
