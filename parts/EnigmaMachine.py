"""
This is body of Enigma Machine which contains 3 Rotors and a wiring board(not implemented yet)
"""
from parts.Rotor import Rotor


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
            r.init(keys[i])
            self.rotors[i] = r
        return None

    def encoding_single_character(self, x):
        y = x
        for i in range(self.rotor_num):
            y = self.rotors[i].encoding_single_character(y)
            if not y:
                return False
        return y

    def decoding_single_character(self, x):
        y = x
        for i in reversed(range(self.rotor_num)):
            y = self.rotors[i].decoding_single_character(y)
            if not y:
                return False
        return y

    def step(self, rotor_index):
        """Recursively progress every rotor"""
        if rotor_index == 0:
            return self.rotors[rotor_index].progression(True)
        return self.rotors[rotor_index].progression(self.step(rotor_index - 1))

    def coding(self, x_sentence: str, encoding=True):
        """
        X -> Y
        Every single chr encoded over, step one on rotors to change the rotation state.(26 Decimal)
        :param x_sentence: The str need to be encoded.
        :return: The str encoded
        """
        if encoding:
            print('start encoding...')
            y_sentence = ''
            for x in x_sentence:
                y = self.encoding_single_character(x)
                if y:
                    y_sentence += y
                    self.step(self.rotor_num - 1)  # forward decimal
                else:
                    y_sentence +=x
            return y_sentence
        else:
            y_sentence = ''
            for x in x_sentence:
                y = self.decoding_single_character(x)
                if y:
                    y_sentence += y
                    self.step(self.rotor_num - 1)  # forward decimal
                else:
                    y_sentence += x
            print('start decoding...')
            return y_sentence