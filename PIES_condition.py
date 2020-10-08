# Initialize two variables with integer vlaues for conditional evaluation
a = 1
b = 2

# Display the results of conditional evaluation
# Descibe the first variable's value
print('\nVariable a is:', 'One' if (a == 1) else 'Not One')
print('Variable a is:', 'Even' if (a % 2 == 0) else 'Odd')

# Display the results of conditional evaluation
# Descibe the second variable's value
print('\nVariable b is:', 'One' if (b == 1) else 'Not One')
print('Variable b is:', 'Even' if (b % 2 == 0) else 'Odd')

# Assign the result of a condiitonal evaluation to a new variable
max = a if (a > b) else b

# Display the assigned result, identifying the greater of the variable values
print('\nGreater Value Is:', max, '\n')
