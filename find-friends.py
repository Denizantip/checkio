def check_connection(network, first, second):
    path2 = set()
    path1 = {network[0].split('-')[0]}
    for friends in network:
        one,two = friends.split("-")
        if one in path1 or two in path1:
            path1.add(one)
            path1.add(two)
        else:
            path2.add(one)
            path2.add(two)
    if first in path1 and second in path1:
        return True
    elif first in path2 and second in path2:
        return True
    else:
        return False
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
