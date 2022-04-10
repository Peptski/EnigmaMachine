from rotor import Rotor
from reflector import Reflector
from enigma import Enigma

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    machine = Enigma()
    rotors = [1, 2, 3]
    while len(rotors):
        version = input("Enter the version of rotor number {0}: ".format(4 - len(rotors)))
        if version in ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]:
            ring = input("Enter the ring setting for rotor {0}: ".format(version))
            if ring in alphabet: ring = alphabet.index(ring) + 1
            else: ring = int(ring)
            if ring > 0 and ring < 27:
                rotor = createRotor(version, ring)
                char = input("Enter the starting character for rotor {0}: ".format(version)).upper()
                if type(char) == int: 
                    if char > 0 and char < 27:
                        char = alphabet[char]
                if char in alphabet:
                    rotor.setChar(char)
                    machine.setRotor(rotors[-1], rotor)
                    rotors.pop()
                else:
                    print("Invalid start character!, retry!\n")
            else:
                print("Invalid ring value!, retry!\n")
        else:
            print("Invalid version of rotor!, retry!\n")

    while machine.rotors[3] == None:
        reflector = input("Select a reflector: ").upper()
        if reflector in ["A", "B", "C"]:
            machine.setReflector(createReflector(reflector))
        else:
            print("Invalid reflector type!")

    pair = ""
    used = []
    while not pair == "DONE":
        pair = input("\nEnter a plugboard pair, or type done: ").upper()
        if len(pair) == 2 and pair[0] in alphabet and pair[1] in alphabet and pair[0] != pair[1] and pair[0] not in used and pair[1] not in used:
            machine.addPlug(pair)
            used.append(pair[0])
            used.append(pair[1])
        else:
            if pair != "DONE":
                print("Invalid pair!")

    file = input("\nEnter the filename of encrypted file: ")
    with open(file, "r") as f:
        data = f.readlines()
    
    newData = ""
    for line in data:
        for char in line:
            char = char.upper()
            if char in alphabet:
                newData += machine.getChar(char.upper())

    print("\n", " ".join(newData[i:i + 5] for i in range(0, len(newData), 5)))

def createReflector(name):
    mappings = {
        "A"     : "EJMZALYXVBWFCRQUONTSPIKHGD",
        "B"     : "YRUHQSLDPXNGOKMIEBFZCWVJAT",
        "C"     : "FVPJIAOYEDRZXWGCTKUQSBNMHL"
    }

    if name in mappings.keys():
        mapping = {alphabet[i] : mappings[name][i] for i in range(0, 26)}
        return Reflector(mapping, mappings[name], name)
    else:
        return None


def createRotor(name, ring):
    ring -= 1
    mappings = {
        "I"     : "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        "II"    : "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        "III"   : "BDFHJLCPRTXVZNYEIWGAKMUSQO",
        "IV"    : "ESOVPZJAYQUIRHXLNFTGKDCMWB",
        "V"     : "VZBRGITYUPSDNHLXAWMJQOFECK",
        "VI"    : "JPGVOUMFYQBENHZRDKASXLICTW",
        "VII"   : "NZJHGRCXMYSWBOUFAIVLPEKQDT",
        "VIII"  : "FKQHTLXOCBJSPDZRAMEWNIUYGV"
    }

    notches = {
        "I"     : ["R"],
        "II"    : ["F"],
        "III"   : ["W"],
        "IV"    : ["K"],
        "V"     : ["A"],
        "VI"    : ["A", "N"],
        "VII"   : ["A", "N"],
        "VIII"  : ["A", "N"]
    }

    if name in mappings.keys():
        mapping = {alphabet[i] : chr(((ord(mappings[name][(i - ring) % 26]) + ring - 65) % 26) + 65) for i in range(0, 26)}
        invMapping = {chr(((ord(mappings[name][(i - ring) % 26]) + ring - 65) % 26) + 65) : alphabet[i] for i in range(0, 26)}
        return Rotor(mapping, invMapping, name, notches[name])
    else:
        return None

main()