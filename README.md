# EnigmaMachine

Enigma encode & decode message from textfile. The supported rotors are the regular five aswell as the more complex navy rotors VI, VII and VIII. The rotors are created in order from left to right (closest to reflector first). 

The format for inputs:
* Rotor version: I, II, III, IV, V, VI, VII, VIII
* Ring value: 0 < x < 27 or A <= x <= Z (Not case sensative)
* Start character: 0 < x < 27 or A <= x <= Z (Not case sensative)

Output is the message or cipher in blocks of five.
