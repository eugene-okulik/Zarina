import random


salary = int(input('Укажите вашу зарплату, $: '))
bonus = random.choice([True, False])
if bonus is True:
    print(f"{salary}, {bonus} - '${salary + random.randrange(1000,2000)}'")
else:
    print(f"{salary}, {bonus} - '${salary}'")
