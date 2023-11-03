import sys


def main():
    '''Count the types of characters in a string'''

    sys.tracebacklimit = 0

    if (len(sys.argv) == 1):
        for line in sys.stdin:
            arg = line
    else:
        assert len(sys.argv) == 2, "Wrong number of arguments"
        arg = sys.argv[1]

    # print(arg)
    total = len(arg)
    upper = len([1 for letter in arg if letter.isupper()])
    lower = len([1 for letter in arg if letter.islower()])
    spaces = len([1 for letter in arg if letter.isspace()])
    digits = len([1 for letter in arg if letter.isdigit()])
    punctuation = total - upper - lower - spaces - digits

    print(f'The text contains {total} characters:')
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(punctuation, "punctuation marks")
    print(spaces, "spaces")
    print(digits, "digits")


if __name__ == "__main__":
    main()
