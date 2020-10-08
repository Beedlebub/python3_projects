numbers = [123, 34, 55, 321, 9]
print(numbers)
print(len(numbers))
print(numbers[0])
print(numbers[1:3])
numbers[0] = 1
print(numbers)
more_numbers = [5, 66, 44]
print(numbers + more_numbers)
numbers_all = numbers + more_numbers
numbers_all.sort()
print(numbers_all)
