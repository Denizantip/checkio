def fib(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a


def checkio(opacity):
    old = [fib(x) for x in range(21)]
    begin = 10000
    x = 1
    while True:
        if x in old:
            begin -= x
        else:
            begin += 1
        if begin == opacity:
            break
        x += 1
    return x

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"