PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''
my_list = PRICE_LIST.split()
my_dict = dict(zip(my_list[0::2], [int(x[:-1]) for x in my_list[1::2]]))
print(my_dict)
