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
        self.current = chr(((ord(self.current) - 64) % 26) + 65)

    def rotateNext(self):
        return self.current in self.notch

    def getChar(self, char, inv, offset):
        if inv: 
            res = chr(((ord(self.invMapping[chr(((offset + (ord(self.current) - 65)) % 26) + 65)]) - ord(self.current)) % 26) + 65)
            offset = (ord(self.invMapping[chr(((offset + (ord(self.current) - 65)) % 26) + 65)]) - ord(self.current)) % 26
            return [res, offset]
        else: 
            res = self.mapping[chr(((offset + (ord(self.current) - 65)) % 26) + 65)]
            offset = ((ord(res) - 65) - (ord(self.current) - 65)) % 26
            return [res, offset]