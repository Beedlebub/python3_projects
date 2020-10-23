import random

random_strength = random.randint(1, 20)
random_dexterity = random.randint(1, 20)
random_constitution = random.randint(1, 20)
random_intelligence = random.randint(1, 20)
random_wisdom = random.randint(1, 20)
random_charisma = random.randint(1, 20)

print('\nRandom Strength Roll: ' + str(random_strength) + '\n')
if random_strength >= 15 and random_strength < 18:
    random_strength += 3
elif random_strength >= 18 and random_strength <= 20:
    random_strength += 5
mod_strength = random_strength
print('Modded Strength Stat: ' + str(mod_strength) + '\n')

#  If battling an Orc, for example, say you must roll using strenth
# You pick the stat you want to use
# DM rolls and then you apply your modifier (as determined above)
# If you beat the static threshold when rolling, you win, if not you lose
# For example Orc requires a Strenth Roll, You have a 7 stat
# You roll an 8, but it applies a minus 5 modifier, which means you ended up rolling a 3 and you lose
