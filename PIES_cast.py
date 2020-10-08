# Initailize two varaiables with numeric values from user input
a = input('\nEnter a number: ')
b = input('Now Enter another number: ')

# Now add the variables together then display the combined
# result and its data type - to see a concatenated string value result
sum = a + b
print('\nData Type sum:', sum, type(sum))

# Add cast variable values together then display the result
# and its data type - to see a total integer value result
sum = int(a) + int(b)
print('\nData Type sum:', sum, type(sum))

# Cast a variable value then display the result
# and its data type - to see a total float value
sum = float(sum)
print('\nData Type sum:', sum, type(sum))

# Cast an integer representation of a variable value then display the result
# and its data type - to see a character string value
sum = chr(int(sum))
print('\nData Type sum:', sum, type(sum), '\n')
