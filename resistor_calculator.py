print('\nResistance Calculator\n')
resistor_one = input('Enter value of first resistor: ')
resistor_two = input('\nEnter value of second resistor: ')
print('\nYou entered', resistor_one, 'and', resistor_two, '\n')
calulation_type = input('Enter "s" for series or "p" for parallel calulation: ')
if calulation_type == "s":
    series_result = int(resistor_one) + int(resistor_two)
    print('The value in series is:', series_result, '\n')
if calculation_type == "p":
    parallel_result = int(resistor_one/1) + int(resistor_two/1)
    print(('The value in parallel is:', parallel_result, '\n')
else if:
    print('Thanks!')