import random

random_constitution = random.randint(1, 20)
random_dexterity = random.randint(1, 20)
random_constitution = random.randint(1, 20)
random_intelligence = random.randint(1, 20)
random_wisdom = random.randint(1, 20)
random_charisma = random.randint(1, 20)


def init_strength():
    global random_constitution
    print('Base Strength Roll: ' + str(random_constitution))
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


def init_dexterity():
    global random_dexterity
    print('Base Dexterity Roll: ' + str(random_dexterity))
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
    print('Base Constitution Roll: ' + str(random_constitution))
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
    print('Base Intelligence Roll: ' + str(random_intelligence))
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
    print('Base Wisdom Roll: ' + str(random_wisdom))
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
    print('Base Charisma Roll: ' + str(random_charisma))
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


def init_stat_mods():
    mod_strength = random_constitution
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


char_name = input('\nHello, adventurer! Please tell me your name: ')
print('\nWelcome, ' + char_name + '! Let\'s roll your character...')
input('Press Enter to continue...')

print()
init_strength()
init_dexterity()
init_constitution()
init_intelligence()
init_wisdom()
init_charisma()
print()
init_stat_mods()

input('Press Enter to continue...')


# # redo this whole progression control
# space = input('Press space to continue...')
# if space != " ":
#     input('Press space to continue...')

  # Wait for the user input to continue or terminate the loop
# while True:
#     ans = input("Do you want do again? (y/n)")
#     # Terminate the script if the input value is 'n'
#     if (ans.lower() == 'n'):
#         break

#  If battling an Orc, for example, say you must roll using strenth
# You pick the stat you want to use
# DM rolls and then you apply your modifier (as determined above)
# If you beat the static threshold when rolling, you win, if not you lose
# For example Orc requires a Strenth Roll, You have a 7 stat
# You roll an 8, but it applies a minus 5 modifier, which means you ended up rolling a 3 and you lose
