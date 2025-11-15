my_dict = {
    'tuple': (1, 2, 'bc',  3, None, 5.5),
    'list': ['abc', 10, False, 11.5, 0, True],
    'dict': {'one': 1, 'two': 2, 'tree': 3, 'four': 4, 'five': 50.5},
    'set': {1, 2, 10, 6, 'abbb'}
}
print((my_dict['tuple'])[-1])
my_dict['list'].append(1111)
my_dict['list'].pop(1)
my_dict['dict']['i am a tuple'] = 999
my_dict['dict'].pop('one')
my_dict['set'].add('pyth')
my_dict['set'].remove(1)
print(my_dict)
