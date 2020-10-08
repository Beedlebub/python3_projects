# simulates six-sided die
from random import randint

# Varaiable for counting times in loop a 6 was rolled
count = 0
# Housekeeping, adds a blank line before output
print('')

# Loop through a random number being generated 10 times
for x in range(1, 11):
    random_number = randint(1, 6)
    print(random_number)
    if random_number == 6:
        count += 1
print('\nTimes a 6 was rolled:', count, '\n')
