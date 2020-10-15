# Create and test a program to check whether a number is even or odd. 

# Hint: you will need to incorporate a variable and some math that looks something like this: 

# rem = usersnum%2   // % means modulus and will return the remainder after dividing

number = input('\nEnter a number and I\'ll tell you if its even or odd: ')
remainder = int(number) % 2

if remainder == 0:
    print('\nYou\'re number, ' + number + ', is an even number!\n')
else:
    print('\nYou\'re number, ' + number + ', is an odd number!\n')
