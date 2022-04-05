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
            res = chr(((ord(self.invMapping[chr(((offset + (ord(self.current) - 65)) % 26) + 65)]) - ord(self.current)) % 26) + 65)
            offset = (ord(self.invMapping[chr(((offset + (ord(self.current) - 65)) % 26) + 65)]) - ord(self.current)) % 26
            return [res, offset]


        else: 
            res = self.mapping[alphabet[(offset + (ord(self.current) - 65)) % 26]]
            offset = (alphabet.index(res) - (ord(self.current) - 65)) % 26
            return [res, offset]