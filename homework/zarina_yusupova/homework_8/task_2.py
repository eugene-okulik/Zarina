def fibonachi(limit=100):
    a = 0
    b = 1
    count1 = 1
    while count < limit:
        yield a
        a, b = b, a + b
        count1 += 1


count = 1
for element in fibonachi(limit=1000000000000):
    if count == 5:
        print(element)
    elif count == 200:
        print(element)
    elif count == 1000:
        print(element)
    elif count == 100000:
        print(element)
    count += 1
