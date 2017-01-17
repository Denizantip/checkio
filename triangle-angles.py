from math import acos as arc_cos, degrees


def cos_theorem(a, b, c): 
    angle = lambda a, b, c: round(degrees(arc_cos((b**2 + c**2 - a**2)/(2 * b * c))))
    return sorted([angle(a, b ,c), angle(b, c, a), angle(c, a, b)])

def checkio(a, b, c):
    if a + b <= c or b + c <= a or a + c <= b:
        return [0, 0, 0]
    return cos_theorem(a, b ,c)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
