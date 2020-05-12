# Roll a 4-, 6-, 8-, 10-, 12-, or 20-sided die
def roll(input_array):
    sides = int(input_array[1])
    possible_sides = set([4, 6, 8, 10, 12, 20])
    if sides in possible_sides:
        print(str(get_roll(sides)))
    else:
        print("Error: This game is only equipped with 4, 6, 8, 10, 12, and 20-sided dice.")


# Calculate a roll of the die
def get_roll(sides):
    return random.randrange(1, sides)