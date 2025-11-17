numbers = list(range(1, 101))
new_numbers = []
for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        new_numbers.append('FuzzBuzz')
    elif number % 3 == 0:
        new_numbers.append('Fuzz')
    elif number % 5 == 0:
        new_numbers.append('Buzz')
    else:
        new_numbers.append(str(number))
print('\n'.join(new_numbers))
