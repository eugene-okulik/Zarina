all_examples = [
    'результат операции: 42',
    'результат операции: 54',
    'результат работы программы: 209',
    'результат: 2'
]


def calc(example):
    result = int(example[example.index(': ') + 2:]) + 10
    return result


for every_example in all_examples:
    print(calc(every_example))
