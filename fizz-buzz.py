def checkio(number):
    if not number % 3:
        if not number % 5:
            return('Fizz Buzz')
        else:
            return('Fizz')
    elif not number % 5 :
        return('Buzz')
    else: 
        return str(number)