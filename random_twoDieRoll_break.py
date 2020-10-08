# simulates two six-sided dice rollaed at same time
import random

count = 0
print('')

while True:
    count += 1
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    total = die_1 + die_2
    print(total)
    if die_1 == 6 and die_2 == 6:
        break
print('\nDouble Sixes thrown!!')
print('Took', count, 'throws to do it!!\n')
