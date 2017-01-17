def checkio(data, s=0):
    if data:
        return checkio(data, s+data.pop())
    else:
        return s
