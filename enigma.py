# Enigma M3
class Enigma:
    rotors = [None, None, None, None]
    plugBoard = {}

    def setRotor(self, num, rotor):
        if num > 0 and num < 4:
            self.rotors[num - 1] = rotor
            print("Rotor version {0} set at position {1}\n".format(rotor.version, num))

    def setReflector(self, reflector):
        self.rotors[3] = reflector
    
    def getRotors(self):
        return len([0 for rotor in self.rotors if rotor != None])

    def addPlug(self, pair):
        if not pair[0] in self.plugBoard.keys() and not pair[1] in self.plugBoard.keys():
                self.plugBoard[pair[0]] = pair[1]
                self.plugBoard[pair[1]] = pair[0]

    def removePlug(self, pair):
        if pair[0] in self.plugBoard.keys() and pair[1] in self.plugBoard.keys():
            if self.plugBoard[pair[0]] == pair[1] and self.plugBoard[pair[1]] == pair[0]:
                self.plugBoard.pop(pair[0], None)
                self.plugBoard.pop(pair[1], None)

    def updateRotor(self, num, char):
        self.rotors[num] = self.rotors[num].setChar(char)

    def getChar(self, char):

        print(self.rotors[0].current, self.rotors[1].current, self.rotors[2].current)

        # Spin rotors
        self.rotors[0].incChar()
        if self.rotors[0].rotateNext():
            self.rotors[1].incChar()
            if self.rotors[1].rotateNext():
                self.rotors[2].incChar()

        print(self.rotors[0].current, self.rotors[1].current, self.rotors[2].current)
        
        # Plugboard
        if char in self.plugBoard.keys():
            char = self.plugBoard[char]
        
        # 1 -> 2 -> 3
        for i in [0, 1, 2]:
            char = self.rotors[i].getChar(char, False)
            print(char)

        # Reflection
        char = self.rotors[3].getChar(char)
        print(char)
        
        # inv(3) -> inv(2) -> inv(1)
        for i in [2, 1, 0]:
            char = self.rotors[i].getChar(char, True)
            print(char)
        
        # Plugboard
        if char in self.plugBoard.keys():
            char = self.plugBoard[char]

        return char
