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
        self.current = alphabet[(ord(self.current) - 64) % 26]

    def rotateNext(self):
        return self.current in self.notch

    def getChar(self, char, inv, offset):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        if inv: 
            res = self.invMapping[alphabet[(offset - (ord(self.current) - 64)) % 26]]
            print(alphabet[(offset - (ord(self.current) - 64)) % 26])
            print(chr(offset + 65))
            print(ord(self.invMapping[char]))
            print(ord(self.invMapping[char]) - 65)
            print(ord(self.current))
            print(ord(self.current) - 65)
            print(res)
            return [res, (ord(self.current) - 64)]


        else: 
            res = self.mapping[alphabet[(offset + (ord(self.current) - 65)) % 26]]
            return [res, ((alphabet.index(res) - (ord(self.current) - 65)) % 26)]

        # P -> N -> G 