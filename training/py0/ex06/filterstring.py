from ft_filter import ft_filter
import sys


def main():
    '''filter words longer than N'''

    sys.tracebacklimit = 0
    assert len(sys.argv) == 3, "the arguments are bad"
    string = sys.argv[1]
    count = sys.argv[2]

    try:
        string = sys.argv[1]
        count = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the argument are bad") from None

    # print(f'{string=} {count=}')
    print(ft_filter(lambda n: len(n) >= count, string.split()))


if __name__ == "__main__":
    main()