"""
    Program: RPG Helper
    Authors: Elizabeth Adams, Ian Jiang
    Copyright: 2020
"""
import sys
import random
import pandas as pd
from classes.character import Character
'''
    Add weapons class
        -attributes: name, damage (ex:3d4+2)
    Add ac (armor class) trait to characters
    Add equip_weapon function to characters
'''


# Roll a 4-, 6-, 8-, 10-, 12-, or 20-sided die
def roll(input_array):
    sides = int(input_array[1])
    possible_sides = set([4, 6, 8, 10, 12, 20])
    if sides in possible_sides:
        print(str(random.randrange(1, sides)))
    else:
        print("Error: This game is only equipped with 4, 6, 8, 10, 12, and 20-sided dice.")


# Add a character to the character array
def new(input_array):
    global characters
    new_char = Character(*input_array[1:])
    characters[new_char.name] = new_char
    print("Huzzah! " + new_char.name + " has joined the game. Welcome to the campaign.")


# Remove a character from the character array
def remove(input_array):
    global characters
    char = characters.pop(input_array[1], "Character not found")
    print("Goodbye, " + char.name)


# Print character stats for a specified character or for all characters
def stats(input_array):
    global characters
    if input_array[1] == "all":
        for c in characters:
            print(characters[c])
    else:
        char = characters[input_array[1]]
        print(char)


# Heal character's HP up to max health
def heal(input_array):
    global characters
    char = characters[input_array[1]]
    char.get_healed(int(input_array[2]))
    print(char.name + " was healed! New HP is " + char.hp)


# Damage character's HP up to 0 (death)
def damage(input_array):
    global characters
    char = characters[input_array[1]]
    char.take_damage(int(input_array[2]))
    if char.hp == 0:
        print(char.name + " has perished!")
    else:
        print(char.name + " took damage! New HP is " + str(char.hp) + "/" + str(char.maxhp))


# Print help text
def help(user_input = "none"):
    help_text = "RPG Helper is a command-line app that handles dice rolls and character stats.\n\n" + \
                "Usage: This app takes a command word followed by parameters as input. The full list of commands " + \
                "can be found below.\n\n" + \
                "roll <number_of_dice_sides>                Roll a dice. Ex: To roll a 6-sided die, enter 'roll 6'\n" + \
                "new <character_name> <maxhp> <hp> <atk>    Add a new character to the campaign.\n" + \
                "stats <character_name>                     View the stats of the specified character.\n" + \
                "stats all                                  View the stats of all characters in the campaign.\n" + \
                "heal <character name> <amount>             Heal a character by a specified amount of HP.\n" + \
                "damage <character name> <amount>           Damage a character by a specified amount of HP.\n" + \
                "help                                       Display help text.\n" + \
                "quit                                       Save to file and quit the session."
    print(help_text)


# Save data and close program
def quit(user_input = "none"):
    save()
    sys.exit(0)


# Save characters data to .csv file
def save(user_input = "none"):
    global characters
    column_names = list(vars(list(characters.values())[0]).keys())
    character_attributes = [list(vars(char).values()) for char in characters.values()]
    pd.DataFrame(character_attributes, columns=column_names).to_csv("characters.csv", index=False)


# Load data from .csv file
def load(user_input = "none"):
    global characters
    df = pd.read_csv("characters.csv")
    columns = df.columns.tolist()
    characters_series = df.apply(lambda x: (x[columns[0]], Character(**dict(x))), axis=1)
    characters = dict(list(characters_series))
    print("Ready players: " + ", ".join(list(characters.keys())))

# Initialize
introText = "RPG Helper \n" + \
            "A one-stop-shop for dice rolls and tracking character stats.\n\n" + \
            "Enter 'help' to see usage details\n\n"
print(introText)

# Load characters data from file
characters = []
load()

# Take user input and execute functions or print error text
while True:
    try:
        user_input = [user_input for user_input in input().split()]
        getattr(sys.modules[__name__], user_input[0])(user_input)
    except AttributeError:
        print("Sorry, I didn't recognize that command. Please find the list of commands below.\n")
        help()
    except IndexError:
        print("Sorry, I think that command was missing an argument. Please find the list of commands below.\n\n")
        help()
