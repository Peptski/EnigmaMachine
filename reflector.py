class Reflector:
    version = ""
    listMapping = []
    mapping = {}

    def __init__(self, mapping, listMapping, version):
        self.version = version
        self.mapping = mapping
        self.listMapping = listMapping

    def getChar(self, char, offset):
        char = self.mapping[chr(offset + 65)]
        offset = ord(self.mapping[chr(offset + 65)]) - 65
        return char, offset