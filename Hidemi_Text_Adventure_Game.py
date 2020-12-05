# Text Adventure Game


name = input("What is your name?")
print("Hi " + name + ", are you ready to learn Python programming?")
print()
print("If so, press Enter to start the adventure.")
print()
print("OK,here we go. Let's learn Python...")
print("with the famous....\n")
print("TEXT ADVENTURE GAME!")
print("\n")

print("""

SCENARIO:

Your Mom is going to make her speciality, a mushroom soup for dinner!
So she asked you to go to a forest nearby for hunting mushrooms.
However, you seems to get lost!
It's getting dark....it's dangerous to stay there in the dark, you need to get out quickly!
I'm your voice in your head, and I'll help you if I can.

""")
print()

input("Press ENTER to continue\n\n")


# Function for the start of the main part of the game
def big_tree ():
    print()
    print("You are in front of a big tree which is 1000 years old.")
    print("You see three paths from here.")
    print("Which direction will you go through: the north (N), east (E) and west (W)?")
    print()
    choice = input("Enter either N, E or W?")

    if choice == "N":
        cave()
    elif choice == "E":
        bridge()
    elif choice == "W":
        abandoned_castle()
    else:
        print("I didn't understand. Let's try this again, you have to get out NOW!")
        big_tree()


# The Cave function
def cave():
    print("\nYou are now in a creepy cave where demons wander around to eat humans. ")
    print("You'll find that there are three gates to the north (N), east (E) and south (S).")
    choice = input("which exit will you go through? Type your choice? (Don't go East!!)")

    if choice == "N":
        print("You pushed the gate door, but it's locked.")
        print("There is a keypad. You need to type a code into it to unlock the door and escape.")
        print("(The code is in one of the rooms in the house.)")
        enter_find = input("Do you want to enter the code (E) or find the code (F)?\n")

        if enter_find == "E":   # Nested IF 
             escape()
        elif enter_find == "F":
             big_tree()
        else:
            print("Sorry, I didn't understand. Let's try this again.")
            cave()

    elif choice == "S":
        big_tree()

    elif choice == "E":
        print("\nYou see a light over there! Keep on walking!")
        print("!!!!!!!!!!!!")
        print("Oh no!! You entered the jungle with full of demons!")
        print("You're........DEAD!\n")
        print("Oh dear " + name + ". Never mind. Do you want to play again?")
        play_again = input('Type "YES" (and press ENTER)to play again, or just press ENTER to end the program.')

        if play_again == "YES":
            print("\n Great! Just remember not to go East this time (I did try to want you :p).") 
            big_tree()
        else:
            exit()
    else:
        print("I didn't understand. Let's try this again, you have to get out NOW!")
        cave()


# Abandoned castle fuction
def abandoned_castle():
    print("\nYou are in an abandoned castle.")
    print("You see heavy wooden doors to the south (S) and west (W)")
    print()
    choice = input("Which door will you go in? Make your choice:")

    if choice == "S":
        dungeon()
    elif choice == "W":
        big_tree()
    else:
        print("Sorry, I didn't understand. Let's try this again.")
        abandoned_castle()


# The dungeon fuction where the user find the second keyword and meet on old guy
def dungeon():
    print("\nIn the Dungeon, you've found an apple on the table.")
    print("You also see an old guy kept in the cell")
    choice = input("Will you talk to the guy? Say Yes (Y) or No (N).")

    if choice == "Y":
        print("The old guy said that 'Remember what you have seen on the table here and another thing in the dwarf house. You need to provide the name of what you saw to get out of this forest.")
        print("Otherwise......you'll be like me!")
        print("Do you understand?")

        confirmation = ""
        while confirmation != "Yes":
            confirmation = input("Confirm (Yes) that you have understood his advice: ")
        print("\nWell done! " + name + ", you're doing great!")
        input("Press ENTER to leave the room.\n")
        abandoned_castle()

    elif choice == "N":
        abandoned_castle()

# The bridge function
def bridge():
    print()
    print("Now you see a wooden bridge. It seems be tremendously old, watch your steps and let's cross the bridge.")
    print()
    choice = input("There are two paths. Which direction will you go? East(E) or South(S)?")

    if choice == "S":
        dwarf_house()
    elif choice == "E":
        big_tree()
    else:
        print("Sorry, I didn't understand. Let's try this again.")
        bridge()


# The dwarf house where the user find the first keyword
def dwarf_house():
    print()
    print("\nYou are in a dwarf house. Seven dwarfs are having a tea party. ")
    choice = input("Do you want to talk to them? Say Yes(Y) or No(N).")

    if choice == "Y":
        print("Hi! You should have come here early!")
        print("Sorry, we finised our cheesecake...")
        print("But I will tell you an important thing.")
        print("This house is made by pine. P-I-N-E. Remeber this! Very important!Okay?")
        
        confirmation = ""
        while confirmation != "Yes":
            confirmation = input("Confirm (Yes) that you have understood: ")
        print("\nWell done! " + name + ", amazing!")
        input("Press ENTER to leave the house.\n")
        bridge()

    elif choice == "N":
        bridge()

       

# Trying to enter the code on the keypad to scape through the North gate
def escape():

    code = ""

    while code != "pineapple":
        code = input("Enter a code:(hint: you need to combine two keywords you found,how to combine? Be creative!)")

        if code == "pineapple":
            print("You're FREE !!!!!!!!")
            print("Surprisingly, you are at in front of your house! Your basket is full of mushrooms too!")
            print("Enjoy your dinner!")
            input("Press ENTER and click OK to end the program.")
            exit()
        else:
            print("Incorrect")
            look_for_code = input("Press Y to look for the code again, or ENTER to try again.")

            if look_for_code == "Y":
                big_tree()
            else:
                look_for_code == ""

    print()
    input("Press ENTER to click OK to end the game.")


# Start of the Game
big_tree()
