class Friends:
    def __init__(self, connections):
        self.connections = connections

    def add(self, connection):
        self.connection = connection
        if self.connection in self.connections:
            return False
        else:
            self.connections += (self.connection,)
            return True

    def remove(self, connection):
        self.connection = connection
        if self.connection in self.connections:
            tupl = tuple()
            for i in self.connections:
                if i != self.connection:
                    tupl += (i,)
                else:
                    continue
            self.connections = tupl
            return True
        else:
            return False

    def names(self):
        n = set()
        for i in self.connections:
            n = n | i
        return n

    def connected(self, name):
        self.name = name
        s = set()
        for i in self.connections:
            if self.name in i:
                s = s | i - {self.name}
        return s



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
