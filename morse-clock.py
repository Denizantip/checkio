def checkio(time_string):
    result = ''
    fill = ((2, 4), (3, 4), (3, 4))
    for n, number in enumerate(time_string.split(':')):
        for n2, char in enumerate(number.zfill(2)):
            result += bin(int(char))[2:].zfill(fill[n][n2]).replace('1', '-').replace('0', '.') + ' '
        result += ': '
    return result[:-3]
    
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

