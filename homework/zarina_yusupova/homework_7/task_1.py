i = 5
while True:
    user_input = int(input('Введите цифру: '))
    if i == user_input:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('Попробуйте снова')
