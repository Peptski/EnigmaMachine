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
        if char in self.mapping.keys():
            self.current = char
            return True
        else:
            print("failed")
            return False

    def incChar(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.current = alphabet[(alphabet.index(self.current) + 1) % 26]

    def rotateNext(self):
        return self.current == self.notch

    def getChar(self, char, inv):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # Safety for reflector
        if self.current in alphabet: current = self.current
        else: current = "A"

        if inv: return self.invMapping[alphabet[(alphabet.index(char) + alphabet.index(current)) % 26]]
        else: return self.mapping[alphabet[(alphabet.index(char) + alphabet.index(current)) % 26]]