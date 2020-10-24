# Python "Random" Dundeons and Dragons

# import library to create random numbers
import random

# store random variables for each of the six player stats
base_strength = random.randint(1, 20)
base_dexterity = random.randint(1, 20)
base_constitution = random.randint(1, 20)
base_intelligence = random.randint(1, 20)
base_wisdom = random.randint(1, 20)
base_charisma = random.randint(1, 20)
# declare variables for stat modifiers
mod_strength = None
mod_dexterity = None
mod_constitution = None
mod_intelligence = None
mod_wisdom = None
mod_charisma = None
# declaring some variables for combat rolls
monster_roll_total = None
player_roll_total = None


# the six functions direclty below do the math for creating a
# mod value based on the random base stats rolled above
def init_strength():
    # Allow variables created in this funtion work in other parts of code
    global mod_strength
    # Follow table given in lesson for what mods to apply
    if base_strength == 1:
        mod_strength = -5
    elif base_strength >= 2 and base_strength < 4:
        mod_strength = -4
    elif base_strength >= 4 and base_strength < 6:
        mod_strength = -3
    elif base_strength >= 6 and base_strength < 8:
        mod_strength = -2
    elif base_strength >= 8 and base_strength < 10:
        mod_strength = -1
    elif base_strength >= 10 and base_strength < 12:
        mod_strength = 0
    elif base_strength >= 12 and base_strength < 14:
        mod_strength = 1
    elif base_strength >= 14 and base_strength < 16:
        mod_strength = 2
    elif base_strength >= 16 and base_strength < 18:
        mod_strength = 3
    elif base_strength >= 18 and base_strength < 20:
        mod_strength = 4
    elif base_strength == 20:
        mod_strength = 5


def init_dexterity():
    global mod_dexterity
    if base_dexterity == 1:
        mod_dexterity = -5
    elif base_dexterity >= 2 and base_dexterity < 4:
        mod_dexterity = -4
    elif base_dexterity >= 4 and base_dexterity < 6:
        mod_dexterity = -3
    elif base_dexterity >= 6 and base_dexterity < 8:
        mod_dexterity = -2
    elif base_dexterity >= 8 and base_dexterity < 10:
        mod_dexterity = -1
    elif base_dexterity >= 10 and base_dexterity < 12:
        mod_dexterity = 0
    elif base_dexterity >= 12 and base_dexterity < 14:
        mod_dexterity = 1
    elif base_dexterity >= 14 and base_dexterity < 16:
        mod_dexterity = 2
    elif base_dexterity >= 16 and base_dexterity < 18:
        mod_dexterity = 3
    elif base_dexterity >= 18 and base_dexterity < 20:
        mod_dexterity = 4
    elif base_dexterity == 20:
        mod_dexterity = 5


def init_constitution():
    global mod_constitution
    if base_constitution == 1:
        mod_constitution = -5
    elif base_constitution >= 2 and base_constitution < 4:
        mod_constitution = -4
    elif base_constitution >= 4 and base_constitution < 6:
        mod_constitution = -3
    elif base_constitution >= 6 and base_constitution < 8:
        mod_constitution = -2
    elif base_constitution >= 8 and base_constitution < 10:
        mod_constitution = -1
    elif base_constitution >= 10 and base_constitution < 12:
        mod_constitution = 0
    elif base_constitution >= 12 and base_constitution < 14:
        mod_constitution = 1
    elif base_constitution >= 14 and base_constitution < 16:
        mod_constitution = 2
    elif base_constitution >= 16 and base_constitution < 18:
        mod_constitution = 3
    elif base_constitution >= 18 and base_constitution < 20:
        mod_constitution = 4
    elif base_constitution == 20:
        mod_constitution = 5


def init_intelligence():
    global mod_intelligence
    if base_intelligence == 1:
        mod_intelligence = -5
    elif base_intelligence >= 2 and base_intelligence < 4:
        mod_intelligence = -4
    elif base_intelligence >= 4 and base_intelligence < 6:
        mod_intelligence = -3
    elif base_intelligence >= 6 and base_intelligence < 8:
        mod_intelligence = -2
    elif base_intelligence >= 8 and base_intelligence < 10:
        mod_intelligence = -1
    elif base_intelligence >= 10 and base_intelligence < 12:
        mod_intelligence = 0
    elif base_intelligence >= 12 and base_intelligence < 14:
        mod_intelligence = 1
    elif base_intelligence >= 14 and base_intelligence < 16:
        mod_intelligence = 2
    elif base_intelligence >= 16 and base_intelligence < 18:
        mod_intelligence = 3
    elif base_intelligence >= 18 and base_intelligence < 20:
        mod_intelligence = 4
    elif base_intelligence == 20:
        mod_intelligence = 5


def init_wisdom():
    global mod_wisdom
    if base_wisdom == 1:
        mod_wisdom = -5
    elif base_wisdom >= 2 and base_wisdom < 4:
        mod_wisdom = -4
    elif base_wisdom >= 4 and base_wisdom < 6:
        mod_wisdom = -3
    elif base_wisdom >= 6 and base_wisdom < 8:
        mod_wisdom = -2
    elif base_wisdom >= 8 and base_wisdom < 10:
        mod_wisdom = -1
    elif base_wisdom >= 10 and base_wisdom < 12:
        mod_wisdom = 0
    elif base_wisdom >= 12 and base_wisdom < 14:
        mod_wisdom = 1
    elif base_wisdom >= 14 and base_wisdom < 16:
        mod_wisdom = 2
    elif base_wisdom >= 16 and base_wisdom < 18:
        mod_wisdom = 3
    elif base_wisdom >= 18 and base_wisdom < 20:
        mod_wisdom = 4
    elif base_wisdom == 20:
        mod_wisdom = 5


def init_charisma():
    global mod_charisma
    if base_charisma == 1:
        mod_charisma = -5
    elif base_charisma >= 2 and base_charisma < 4:
        mod_charisma = -4
    elif base_charisma >= 4 and base_charisma < 6:
        mod_charisma = -3
    elif base_charisma >= 6 and base_charisma < 8:
        mod_charisma = -2
    elif base_charisma >= 8 and base_charisma < 10:
        mod_charisma = -1
    elif base_charisma >= 10 and base_charisma < 12:
        mod_charisma = 0
    elif base_charisma >= 12 and base_charisma < 14:
        mod_charisma = 1
    elif base_charisma >= 14 and base_charisma < 16:
        mod_charisma = 2
    elif base_charisma >= 16 and base_charisma < 18:
        mod_charisma = 3
    elif base_charisma >= 18 and base_charisma < 20:
        mod_charisma = 4
    elif base_charisma == 20:
        mod_charisma = 5

# on my next iterarion I am going to add all of the stats to a
# 'list' and enemurate them with a 'for' loop
# I could get away with a single function, maybe two to do what I did in
# seven functions


def print_base_stats():
    # function to block print the player's base stats
    print('Base Strength Roll:\t' + str(base_strength))
    print('Base Dexterity Roll:\t' + str(base_dexterity))
    print('Base Constitution Roll:\t' + str(base_constitution))
    print('Base Intelligence Roll:\t' + str(base_intelligence))
    print('Base Wisdom Roll:\t' + str(base_wisdom))
    print('Base Charisma Roll:\t' + str(base_charisma))


def print_modded_stats():
    # Then we then print all the modifiers out, right below the base stats
    print('Strength Modifier:\t' + str(mod_strength))
    print('Dexterity Modifier:\t' + str(mod_dexterity))
    print('Constitution Modifier:\t' + str(mod_constitution))
    print('Intelligence Modifier:\t' + str(mod_intelligence))
    print('Wisdom Modifier:\t' + str(mod_wisdom))
    print('Charisma Modifier:\t' + str(mod_charisma))


def print_all_stats():
    # print out out all player stats
    # next iteration , this will be removed or shortened
    print()
    print_base_stats()
    init_strength()
    init_dexterity()
    init_constitution()
    init_intelligence()
    init_wisdom()
    init_charisma()
    print()
    print_modded_stats()
    print()


##### start main game loop
##### next iterarion, this will be broken into functions


# get player's name
char_name = input('\nHello, adventurer! Please tell me your name: ')
print('\nWelcome, ' + char_name + '! Let\'s roll your character...')
# # ask user to press enter
input('Press Enter to continue...')
# we roll stats, apply mods, and print them all out
print_all_stats()
# ask user to press enter one more time before starting combat
input('Press Enter to continue...')

# engage enemy
# On subsequent iterarions, there will be array of random monsters, with their own stats
# players will also be able to do more
print('\nOut of nowhere, a large brute of an Orc leaps out at you.\n')
monster_combat_die_one = random.randint(1, 10)
monster_combat_die_two = random.randint(1, 10)
monster_roll_total = monster_combat_die_one + monster_combat_die_two
# debug stat
# print(str(monster_roll_total) + '\n')

# this section of code asks user to input stat they want to use for combat
# in further iterations, there will be error checking to make sure only correct values can be input
stat_choice = input(
    'Enter the first two letters of the stat you\'d like to use \nfor combat (ex. co for Constitution): ')
player_combat_roll = random.randint(1, 20)
if stat_choice == 'st':
    player_roll_total = player_combat_roll + mod_strength
    print('\nPlayer Combat Roll:\t' + str(player_combat_roll))
    print('Strength Modifier:\t' + str(mod_strength))
    print('Total Combat Roll:\t' + str(player_roll_total))
elif stat_choice == 'de':
    player_roll_total = player_combat_roll + mod_dexterity
    print('\nPlayer Combat Roll:\t' + str(player_combat_roll))
    print('Dexterity Modifier:\t' + str(mod_dexterity))
    print('Total Combat Roll:\t' + str(player_roll_total))
elif stat_choice == 'co':
    player_roll_total = player_combat_roll + mod_constitution
    print('\nPlayer Combat Roll:\t' + str(player_combat_roll))
    print('Constitution Modifier:\t' + str(mod_constitution))
    print('Total Combat Roll:\t' + str(player_roll_total))
elif stat_choice == 'in':
    player_roll_total = player_combat_roll + mod_intelligence
    print('\nPlayer Combat Roll:\t' + str(player_combat_roll))
    print('Intelligence Modifier:\t' + str(mod_intelligence))
    print('Total Combat Roll:\t' + str(player_roll_total))
elif stat_choice == 'wi':
    player_roll_total = player_combat_roll + mod_wisdom
    print('\nPlayer Combat Roll:\t' + str(player_combat_roll))
    print('Wisdom Modifier:\t' + str(mod_wisdom))
    print('Total Combat Roll:\t' + str(player_roll_total))
elif stat_choice == 'ch':
    player_roll_total = player_combat_roll + mod_charisma
    print('\nPlayer Combat Roll:\t' + str(player_combat_roll))
    print('Charisma Modifier:\t' + str(mod_charisma))
    print('Total Combat Roll:\t' + str(player_roll_total))

print('\nThe Orc rolled a ' + str(monster_roll_total) +
      ' and your total combat roll was ' + str(player_roll_total) + '.')
if player_roll_total > monster_roll_total:
    print('You slayed the Orc and live to fight another day!\n')
elif player_roll_total < monster_roll_total:
    print('The Orc cuts you down where you stand. So sad.\n')
elif player_roll_total == monster_roll_total:
    print('You both land fatal blows and take leave of this world.\n')
