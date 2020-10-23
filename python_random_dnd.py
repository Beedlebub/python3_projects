import random

random_strength = random.randint(1, 20)
random_dexterity = random.randint(1, 20)
random_constitution = random.randint(1, 20)
random_intelligence = random.randint(1, 20)
random_wisdom = random.randint(1, 20)
random_charisma = random.randint(1, 20)


def init_strength():
    global random_strength
    print('Base Strength Roll: ' + str(random_strength))
    if random_strength >= 15 and random_strength < 18:
        random_strength += 3
    elif random_strength >= 18 and random_strength <= 20:
        random_strength += 5


def init_dexterity():
    global random_dexterity
    print('Base Dexterity Roll: ' + str(random_dexterity))
    if random_dexterity >= 15 and random_dexterity < 18:
        random_dexterity += 3
    elif random_dexterity >= 18 and random_dexterity <= 20:
        random_dexterity += 5


def init_constitution():
    global random_constitution
    print('Base Constitution Roll: ' + str(random_constitution))
    if random_constitution >= 15 and random_constitution < 18:
        random_constitution += 3
    elif random_constitution >= 18 and random_constitution <= 20:
        random_constitution += 5


def init_intelligence():
    global random_intelligence
    print('Base Intelligence Roll: ' + str(random_intelligence))
    if random_intelligence >= 15 and random_intelligence < 18:
        random_intelligence += 3
    elif random_intelligence >= 18 and random_intelligence <= 20:
        random_intelligence += 5


def init_wisdom():
    global random_wisdom
    print('Base Wisdom Roll: ' + str(random_wisdom))
    if random_wisdom >= 15 and random_wisdom < 18:
        random_wisdom += 3
    elif random_wisdom >= 18 and random_wisdom <= 20:
        random_wisdom += 5


def init_charisma():
    global random_charisma
    print('Base Charisma Roll: ' + str(random_charisma))
    if random_charisma >= 15 and random_charisma < 18:
        random_charisma += 3
    elif random_charisma >= 18 and random_charisma <= 20:
        random_charisma += 5


def init_stat_mods():
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

# # redo this whole progression control
# space = input('Press space to continue...')
# if space != " ":
#     input('Press space to continue...')

  # Wait for the user input to continue or terminate the loop
while True:
    ans = input("Do you want do again? (y/n)")
    # Terminate the script if the input value is 'n'
    if (ans.lower() == 'n'):
        break

#  If battling an Orc, for example, say you must roll using strenth
# You pick the stat you want to use
# DM rolls and then you apply your modifier (as determined above)
# If you beat the static threshold when rolling, you win, if not you lose
# For example Orc requires a Strenth Roll, You have a 7 stat
# You roll an 8, but it applies a minus 5 modifier, which means you ended up rolling a 3 and you lose
