class Rotor:
    version = ""
    mapping = {}
    invMapping = {}
    current = ""
    notch = ""

    def __init__(self, mapping, invMapping, version, notch):
        self.version = version
        self.mapping = mapping
        self.invMapping = invMapping
        self.notch = notch

    def setChar(self, char):
        self.current = char

    def incChar(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.current = alphabet[(alphabet.index(self.current) + 1) % 26]

    def rotateNext(self):
        return self.current in self.notch

    def getChar(self, char, inv, offset):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        if inv: 
            res = self.invMapping[chr(((ord(char) - ord(self.current) -1) % 26) + 65)]
            print(self.invMapping[char])
            print(ord(self.invMapping[char]))
            print(ord(self.invMapping[char]) - 65)
            print(ord(self.current))
            print(ord(self.current) - 65)


        else: res = self.mapping[alphabet[(offset + alphabet.index(self.current)) % 26]]
        return [res, ((alphabet.index(res) - alphabet.index(self.current)) % 26)]