def checkio(data):
    result = []
    for i in data:
        if data.count(i) >= 2:
            result.append(i)
    return result