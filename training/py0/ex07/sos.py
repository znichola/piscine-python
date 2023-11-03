import sys


def main():
    sys.tracebacklimit = 0

    NESTED_MORSE = {" ": "/ ",
                    "A": ".-",
                    "E": ".",
                    "I": "..",
                    "M": "--",
                    "Q": "--.-",
                    "U": "..-",
                    "Y": "-.--",
                    "B": "-...",
                    "F": "..-.",
                    "J": ".---",
                    "N": "-.",
                    "R": ".-.",
                    "V": "...-",
                    "Z": "--..",
                    "C": "-.-.",
                    "G": "--.",
                    "K": "-.-",
                    "O": "---",
                    "S": "...",
                    "W": ".--",
                    "D": "-..",
                    "H": "....",
                    "L": ".-..",
                    "P": ".--.",
                    "T": "-",
                    "X": "-..-",
                    "A": ".-",
                    "0": "-----",
                    "3": "...--",
                    "6": "-....",
                    "9": "----.",
                    "1": ".----",
                    "4": "....-",
                    "7": "--...",
                    "2": "..---",
                    "5": ".....",
                    "8": "---.."}

    def fl(s):
        return str.isalnum(s) or str.isalnum(s) or s == ' '

    if (len(sys.argv) != 2 or
            len(list(filter(fl, sys.argv[1])))) != len(sys.argv[1]):
        raise AssertionError("the arguments are bad")

    print(" ".join([NESTED_MORSE[char.upper()] for char in sys.argv[1]]))


if __name__ == "__main__":
    main()
