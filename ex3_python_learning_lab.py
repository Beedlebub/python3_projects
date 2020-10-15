name = input('\nPlease enter your name: ')
print('\nHello, ' + name + '!\n')
age = input('Now, please input your age: ')
print('\nHere\'s some fun info...\n')
if int(age) >= 21:
    print(name + ', you\'re old enough to drink alcohol!')
lucky_num = int(age) + 1
print('You\'re lucky number is: ' + str(lucky_num))
divide_by_three = round(int(age) / 3, 2)
print('You\'re age divided by 3 is: ' + str(divide_by_three))
print(name + ', you\'re name is ' + str(len(name)) + ' letters long!')
print('\n')
