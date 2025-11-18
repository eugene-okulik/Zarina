example_1 = 'результат операции: 42'
example_2 = 'результат операции: 514'
example_3 = 'результат работы программы: 9'
print(int(example_1[example_1.index(": ") + 2:]) + 10)
print(int(example_2[example_2.index(": ") + 2:]) + 10)
print(int(example_3[example_3.index(": ") + 2:]) + 10)
