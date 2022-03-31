class Reflector:
    version = ""
    mapping = {}

    def __init__(self, mapping, version):
        self.version = version
        self.mapping = mapping

    def getChar(self, char):
        return self.mapping[char]