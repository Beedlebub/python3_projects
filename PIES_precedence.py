# Initialize variables with integer values for precedence comparision
a = 2
b = 4
c = 8

# Display the results of default precedence and forcing
# addition before multiplication
print('\nDefault Order:\t', a, '*', c, '+', b, '=', a * c + b)
print('Forced Order:\t', a, '* (', c, '+', b, ') =', a * (c + b))

# Display the results of default precedence and forcing
# subtraction before division
print('\nDefault Order:\t', c, '//', b, '-', a, '=', c // b - a)
print('Forced Order:\t', c, '// (', b, '-', a, ') =', c // (b - a))

# Display the results of default precedence and forcing
# addition before modulus operation
print('\nDefault Order:\t', c, '%', a, '+', b, '=', c % a + b)
print('Forced Order:\t', c, '% (', a, '+', b, ') =', c % (a + b))

# Display the results of default precedence and forcing
# addition before exponent operation
print('\nDefault Order:\t', c, '**', a, '+', b, '=', c ** a + b)
print('Forced Order:\t', c, '** (', a, '+', b, ') =', c ** (a + b), '\n')
