class Reflector:
    version = ""
    listMapping = []
    mapping = {}

    def __init__(self, mapping, listMapping, version):
        self.version = version
        self.mapping = mapping
        self.listMapping = listMapping

    def getChar(self, char, offset):
        offset = ((ord(char) - 65) - (offset - self.listMapping.index(chr(offset + 65)))) % 26
        char = chr(offset + 65)
        return char, offset