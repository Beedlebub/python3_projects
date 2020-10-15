# Write a program (open a file, not the command line) that asks a user for two numbers (between 1 and 100). 
# •	If the addition of their numbers is greater than 100, you will let them know they picked high numbers. 
# •	If their sum is less than 100, let them know they picked low numbers. 
# •	If their sum is exactly 100, let them know they picked magic numbers.

print('\nHello! Please enter two numbers (between 1 and 100).\n')
num_one = input('Enter your first number:\t')
num_two = input('Enter your second number:\t')
total = int(num_one) + int(num_two)
if total > 100:
    print('The total of your numbers is:\t' + str(total))
    print('Your number choices included at least one high number.\n')
elif total < 100:
    print('The total of your numbers is:\t' + str(total))
    print('Your number choices included at least one low number.\n')
elif total == 100:
    print('The total of your numbers is:\t' + str(total) + '!!!')
    print('Your selected all magic numbers!\n')
