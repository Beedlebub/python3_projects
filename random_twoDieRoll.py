# simulates two six-sided dice rollaed at same time
import random

print('')

for x in range(1, 11):
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    total = die_1 + die_2
    print(total)
    if total == 7:
        print('Seven Thrown!\t', die_1, 'and', die_2, '\n')
    if total == 11:
        print('Eleven Thrown!\t', die_1, 'and', die_2, '\n')
    if die_1 == die_2:
        print('Doubles Thrown!\t', die_1, 'and', die_2, '\n')

print('')       
