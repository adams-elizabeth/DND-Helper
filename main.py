"""
    Program: RPG Helper
    Authors: Elizabeth Adams, Ian Jiang
    Copyright: 2020
"""
import sys
import random
import pandas as pd
from classes.character import Character

# Initialize
introText = "RPG Helper \n" + \
            "A one-stop-shop for dice rolls and tracking character stats.\n\n" + \
            "Enter 'help' to see usage details\n\n"
print(introText)
'''
    ToDo: Read and write characters to csv file to preserve data between sessions
    Add weapons class
        -attributes: name, damage (ex:3d4+2)
    Add ac (armor class) trait to characters
    Add equip_weapon function to characters
'''


def roll(input_array):
    sides = int(input_array[1])
    possible_sides = set([4, 6, 8, 10, 12, 20])
    if sides in possible_sides:
        print(str(random.randrange(1, sides)))
    else:
        print("Error: This game is equipped with 4, 6, 8, 10, 12, and 20-sided dice.")


def new(input_array):
    global characters
    new_char = Character(input_array[1], input_array[2], input_array[3])
    characters[new_char.get_name()] = new_char
    print("Huzzah! " + new_char.get_name() + " has joined the game. Welcome to the campaign.")


def stats(input_array):
    global characters
    char = characters[input_array[1]]
    print(char.get_name() + "'s HP is " + char.get_hp() + " & Attack is " + char.get_atk())


def heal(input_array):
    global characters
    char = characters[input_array[1]]
    char.get_healed(int(input_array[2]))
    print(char.get_name() + " was healed! New HP is " + char.get_hp())


def damage(input_array):
    global characters
    char = characters[input_array[1]]
    char.take_damage(int(input_array[2]))
    if char.hp == 0:
        print(char.get_name() + " has perished!")
    else:
        print(char.get_name() + " took damage! New HP is " + char.get_hp())


def help(user_input):
    help_text = "Welcome to the RPG Helper, a command-line app that handles dice rolls and character stats\n" + \
                "usage:\n" + \
                "roll [number of dice sides]\n" + \
                "new [character name] [hp] [atk]\n" + \
                "stats [character name]\n" + \
                "heal [character name] [amount]\n" + \
                "damage [character name] [amount]\n" + \
                "help\n" + \
                "quit"
    print(help_text)


def quit(user_input):
    sys.exit(0)


def save(user_input):
    global characters
    column_names = list(vars(list(characters.values())[0]).keys())
    character_attributes = [list(vars(char).values()) for char in characters.values()]
    pd.DataFrame(character_attributes, columns=column_names).to_csv("characters.csv", index=False)


def load(user_input):
    global characters
    df = pd.read_csv("characters.csv")
    columns = df.columns.tolist()
    characters_series = df.apply(lambda x: (x[columns[0]], Character(x[columns[0]], x[columns[1]], x[columns[2]])), axis=1)
    characters = dict(list(characters_series))
    print("Ready players: " + ", ".join(list(characters.keys())))


while True:
    try:
        user_input = [user_input for user_input in input().split()]
        getattr(sys.modules[__name__], user_input[0])(user_input)
    except AttributeError:
        print("Sorry, I didn't recognize that command. Enter 'help' for usage details")
