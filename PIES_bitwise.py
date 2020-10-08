# Initialize two variables with numeric values and display them
a = 10
b = 5
print('\na =', a, '\tb =', b)

# Add a statement to change first variable's decimal value by binary
# bit manipulation
# 1010 ^ 0101 = 1111 (decimal 15)
a = a ^ b

# Add a statement to change second variable's decimal value by binary
# bit manipulation
# 1111 ^ 0101 = 1010 (decimal 10)
b = a ^ b

# Add a statement to change first variable's decimal value once more by
# further bit manipulation
# 1111 ^ 1010 = 0101 (decimal 5)
a = a ^ b

# Add a stement to display the exchanged values
print('a =', a, '\tb =', b, '\n')
