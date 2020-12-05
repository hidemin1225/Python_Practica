# Ask a user to name one of the Olympic medals (Gold, Silver, Bronze)

print("Name one of the colors of Olympic medals!")
medal = input()


if medal.lower() in ["gold", "silver", "bronze"]:
    print("Awesome! You are absolutely right!")
else:
    while medal.lower() != ["gold", "silver", "bronze"]:
        print("Are you sure? Try again?")
