# Iniatialize a list of three elements containing string values
quarter = ['January', 'February', 'March']

# Individually display the value contained in each list element
print('\nFirst Month:\t', quarter[0])
print('Second Month:\t', quarter[1])
print('Third Month:\t', quarter[2])

# Create a multi-dimensional list of two elements, which
# themselves are lists that each have three elements containing
# integer values
coords = [[1, 2, 3],
          [4, 5, 6]]

# Display the values contained in two specific inner list elements
print('\nTop Left Element (0, 0):\t', coords[0][0])
print('Bottom Left Element (1, 2):\t', coords[1][2])

# Display just one character of a string value
print('\nSecond Month, Last Letter:\t', quarter[1][7], '\n')
