"""
This is body of Enigma Machine which contains 3 Rotors and a wiring board(not implemented yet)
"""
from Rotor import Rotor


class EnigmaMachine(object):
    def __init__(self, keys: str):
        """
        :param keys: keys for encoding and decoding
        """
        self.keys = keys
        self.rotor_num = len(keys)
        self.rotors = [None for _ in range(self.rotor_num)]
        self.init(self.keys)

    def init(self, keys: str):
        """
        Create a EnigmaMachine.
        The machine has len(keys) rotors.
        :param keys: A Capital Str that for encoding and decoding
        :return: None
        """
        for i in range(self.rotor_num):
            r = Rotor(i)
            self.rotors[i] = r


if __name__ == '__main__':
    e = EnigmaMachine('ABC')