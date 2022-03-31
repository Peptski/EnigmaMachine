from rotor import Rotor
from enigma import Enigma

def main():
    machine = Enigma()
    rotors = 0
    while rotors < 3:
        print("Enter the version of rotor number {0}".format(rotors + 1))
        version = input()
        if version in ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]:
            print("Enter the ring setting for rotor {0}".format(version))
            index = int(input())
            if index > 0 and index < 27:
                rotor = createRotor(version, index)
                print("Enter the starting character for rotor {0}".format(version))
                char = input().upper()
                res = rotor.setChar(char)
                if res:
                    machine.setRotor(rotors + 1, rotor)
                    rotors += 1
                else:
                    print("Invalid start character!")
            else:
                print("Invalid ring value!")
        else:
            print("Invalid version of rotor!")

    while machine.rotors[3] == None:
        print("Select a reflector")
        reflector = input().upper()
        if reflector in ["A", "B", "C"]:
            machine.setRotor(4, createRotor(reflector, 1))

    pair = ""
    while not pair == "DONE":
        print("Enter a plugboard pair, or type done")
        pair = input().upper()
        if len(pair) == 2:
            #Does not check if alphabetical character
            machine.addPlug(pair)

    print("\nEnter the filename of encrypted file")
    file =  input()
    with open(file, "r") as f:
        data = f.readlines()
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    newData = ""
    for line in data:
        for char in line:
            char = char.upper()
            if char in alphabet:
                print("Character: {0}".format(char.upper()))
                newData += machine.getChar(char.upper())
                print(newData[-1])

    print(newData)

def createRotor(name, ring):
    alphabet =    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mappings = {
        "I"     : "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        "II"    : "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        "III"   : "BDFHJLCPRTXVZNYEIWGAKMUSQO",
        "IV"    : "ESOVPZJAYQUIRHXLNFTGKDCMWB",
        "V"     : "VZBRGITYUPSDNHLXAWMJQOFECK",
        "VI"    : "JPGVOUMFYQBENHZRDKASXLICTW",
        "VII"   : "NZJHGRCXMYSWBOUFAIVLPEKQDT",
        "VIII"  : "FKQHTLXOCBJSPDZRAMEWNIUYGV",
        "A"     : "EJMZALYXVBWFCRQUONTSPIKHGD",
        "B"     : "YRUHQSLDPXNGOKMIEBFZCWVJAT",
        "C"     : "FVPJIAOYEDRZXWGCTKUQSBNMHL"
    }

    notches = {
        "I"     : "R",
        "II"    : "F",
        "III"   : "W",
        "IV"    : "K",
        "V"     : "A",
        "VI"    : "AN",
        "VII"   : "AN",
        "VIII"  : "AN",
        "A"     : "",
        "B"     : "",
        "C"     : ""
    }

    if name in mappings.keys():
        mapping = {alphabet[i] : mappings[name][(i + ring - 1) % 26] for i in range(0, 26)}
        invMapping = {mappings[name][(i + ring - 1) % 26] : alphabet[i] for i in range(0, 26)}
        return Rotor(mapping, invMapping, name, notches[name])
    else:
        return None

main()