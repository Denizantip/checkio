def checkio(number):
    pro = 1
    number = str(number).replace('0','')
    for ch in number:
        pro *= int(ch)
    return pro
    
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
