# Python "Random" Dundeons and Dragons

# import library to create random numbers
import random

# store random variables for each of the six player stats
random_strength = random.randint(1, 20)
random_dexterity = random.randint(1, 20)
random_constitution = random.randint(1, 20)
random_intelligence = random.randint(1, 20)
random_wisdom = random.randint(1, 20)
random_charisma = random.randint(1, 20)

base_strength = random_strength


# the six functions direclty below do the math for applying a
# mod value to the random base stats rolled above
def init_strength():
    # Allow variables created in this funtion work in other parts of code
    global random_strength
    # Follow table for what mods to apply given in lesson
    
    
    
    
    
    
    # try saving random as base
    # try chacking base value and adding to modded value not to base
    # orc rolls 2d10
    # player rolls after picking stat, we need to keep his base sta around
    # maybe creat a static mod value for each base stat value:
    # if base strength == 1
    # mod_strength - -5
    # after player rolls in combat we know we then have a 
    # static mod vale to apply to roll
    
    if random_strength == 1:
        random_strength -= 5
    elif random_strength >= 2 and random_strength < 4:
        random_strength -= 4
    elif random_strength >= 4 and random_strength < 6:
        random_strength -= 3
    elif random_strength >= 6 and random_strength < 8:
        random_strength -= 2
    elif random_strength >= 8 and random_strength < 10:
        random_strength -= 1
    elif random_strength >= 10 and random_strength < 12:
        random_strength += 0
    elif random_strength >= 12 and random_strength < 14:
        random_strength += 1
    elif random_strength >= 14 and random_strength < 16:
        random_strength += 2
    elif random_strength >= 16 and random_strength < 18:
        random_strength += 3
    elif random_strength >= 18 and random_strength < 20:
        random_strength += 4
    elif random_strength == 20:
        random_strength += 5


def init_dexterity():
    global random_dexterity
    if random_dexterity == 1:
        random_dexterity -= 5
    elif random_dexterity >= 2 and random_dexterity < 4:
        random_dexterity -= 4
    elif random_dexterity >= 4 and random_dexterity < 6:
        random_dexterity -= 3
    elif random_dexterity >= 6 and random_dexterity < 8:
        random_dexterity -= 2
    elif random_dexterity >= 8 and random_dexterity < 10:
        random_dexterity -= 1
    elif random_dexterity >= 10 and random_dexterity < 12:
        random_dexterity += 0
    elif random_dexterity >= 12 and random_dexterity < 14:
        random_dexterity += 1
    elif random_dexterity >= 14 and random_dexterity < 16:
        random_dexterity += 2
    elif random_dexterity >= 16 and random_dexterity < 18:
        random_dexterity += 3
    elif random_dexterity >= 18 and random_dexterity < 20:
        random_dexterity += 4
    elif random_dexterity == 20:
        random_dexterity += 5


def init_constitution():
    global random_constitution
    if random_constitution == 1:
        random_constitution -= 5
    elif random_constitution >= 2 and random_constitution < 4:
        random_constitution -= 4
    elif random_constitution >= 4 and random_constitution < 6:
        random_constitution -= 3
    elif random_constitution >= 6 and random_constitution < 8:
        random_constitution -= 2
    elif random_constitution >= 8 and random_constitution < 10:
        random_constitution -= 1
    elif random_constitution >= 10 and random_constitution < 12:
        random_constitution += 0
    elif random_constitution >= 12 and random_constitution < 14:
        random_constitution += 1
    elif random_constitution >= 14 and random_constitution < 16:
        random_constitution += 2
    elif random_constitution >= 16 and random_constitution < 18:
        random_constitution += 3
    elif random_constitution >= 18 and random_constitution < 20:
        random_constitution += 4
    elif random_constitution == 20:
        random_constitution += 5


def init_intelligence():
    global random_intelligence
    if random_intelligence == 1:
        random_intelligence -= 5
    elif random_intelligence >= 2 and random_intelligence < 4:
        random_intelligence -= 4
    elif random_intelligence >= 4 and random_intelligence < 6:
        random_intelligence -= 3
    elif random_intelligence >= 6 and random_intelligence < 8:
        random_intelligence -= 2
    elif random_intelligence >= 8 and random_intelligence < 10:
        random_intelligence -= 1
    elif random_intelligence >= 10 and random_intelligence < 12:
        random_intelligence += 0
    elif random_intelligence >= 12 and random_intelligence < 14:
        random_intelligence += 1
    elif random_intelligence >= 14 and random_intelligence < 16:
        random_intelligence += 2
    elif random_intelligence >= 16 and random_intelligence < 18:
        random_intelligence += 3
    elif random_intelligence >= 18 and random_intelligence < 20:
        random_intelligence += 4
    elif random_intelligence == 20:
        random_intelligence += 5


def init_wisdom():
    global random_wisdom
    if random_wisdom == 1:
        random_wisdom -= 5
    elif random_wisdom >= 2 and random_wisdom < 4:
        random_wisdom -= 4
    elif random_wisdom >= 4 and random_wisdom < 6:
        random_wisdom -= 3
    elif random_wisdom >= 6 and random_wisdom < 8:
        random_wisdom -= 2
    elif random_wisdom >= 8 and random_wisdom < 10:
        random_wisdom -= 1
    elif random_wisdom >= 10 and random_wisdom < 12:
        random_wisdom += 0
    elif random_wisdom >= 12 and random_wisdom < 14:
        random_wisdom += 1
    elif random_wisdom >= 14 and random_wisdom < 16:
        random_wisdom += 2
    elif random_wisdom >= 16 and random_wisdom < 18:
        random_wisdom += 3
    elif random_wisdom >= 18 and random_wisdom < 20:
        random_wisdom += 4
    elif random_wisdom == 20:
        random_wisdom += 5


def init_charisma():
    global random_charisma
    if random_charisma == 1:
        random_charisma -= 5
    elif random_charisma >= 2 and random_charisma < 4:
        random_charisma -= 4
    elif random_charisma >= 4 and random_charisma < 6:
        random_charisma -= 3
    elif random_charisma >= 6 and random_charisma < 8:
        random_charisma -= 2
    elif random_charisma >= 8 and random_charisma < 10:
        random_charisma -= 1
    elif random_charisma >= 10 and random_charisma < 12:
        random_charisma += 0
    elif random_charisma >= 12 and random_charisma < 14:
        random_charisma += 1
    elif random_charisma >= 14 and random_charisma < 16:
        random_charisma += 2
    elif random_charisma >= 16 and random_charisma < 18:
        random_charisma += 3
    elif random_charisma >= 18 and random_charisma < 20:
        random_charisma += 4
    elif random_charisma == 20:
        random_charisma += 5

# this function applies the mod values to the base score
# on my next iterarion i am going to add all of the stats to a
# 'list' and enemurate them with a 'for' loop
# I could get away with a single function, maybe two to do what I did in
# seven functions

def print_base_stats():
    # function to block print the player's base stats
    print('Base Strength Roll: ' + str(random_strength))
    print('Base Dexterity Roll: ' + str(random_dexterity))
    print('Base Constitution Roll: ' + str(random_constitution))
    print('Base Intelligence Roll: ' + str(random_intelligence))
    print('Base Wisdom Roll: ' + str(random_wisdom))
    print('Base Charisma Roll: ' + str(random_charisma))


def print_modded_stats():
    # each line below creates a neqw variable for the modded stats
    # we then print them all out, right below the base stats
    mod_strength = random_strength
    print('Modded Strength: ' + str(mod_strength))
    mod_dexterity = random_dexterity
    print('Modded Dexterity: ' + str(mod_dexterity))
    mod_constitution = random_constitution
    print('Modded Constitution: ' + str(mod_constitution))
    mod_intelligence = random_intelligence
    print('Modded Intelligence: ' + str(mod_intelligence))
    mod_wisdom = random_wisdom
    print('Modded Wisdom: ' + str(mod_wisdom))
    mod_charisma = random_charisma
    print('Modded Charisma: ' + str(mod_charisma))
    print()


def all_stats():
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

# start main game loop
# next iterarion, this will be broken into functions

# get player's name
char_name = input('\nHello, adventurer! Please tell me your name: ')
print('\nWelcome, ' + char_name + '! Let\'s roll your character...')
# ask user to press enter
input('Press Enter to continue...')
# we roll stats, apply mods, and print them all out
all_stats()
# aske user to press enter one more time before starting combat
input('Press Enter to continue...')
# engage enemy
# On subsequent iterarions, there will be array of random monsters
# players will also be able to do more 
print('\nOut of nowhere, a large brute of an Orc leaps out at you.\n')
stat_choice = input('Please enter the first two letters of the stat you\'d like to use for combat (ex. co for Constitution): ')

monster_stat = 15

# if stat_choice = st:
    

#  If battling an Orc, for example, say you must roll using strenth
# You pick the stat you want to use
# DM rolls and then you apply your modifier (as determined above)
# If you beat the static threshold when rolling, you win, if not you lose
# For example Orc requires a Strenth Roll, You have a 7 stat
# You roll an 8, but it applies a minus 5 modifier, which means you ended up rolling a 3 and you lose
