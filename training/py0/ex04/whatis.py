import sys

sys.tracebacklimit = 0

if (len(sys.argv) == 1):
    print("")
    exit()

if (sys.argv[1] == "0"):
    print("I'm Even.")
    exit()

assert len(sys.argv) == 2, "more then one argument is provided"

try:
    assert isinstance(int(sys.argv[1]), int)
except (ValueError, AssertionError):
    print("AssertionError: argument is not an integer")
    exit()


print("I'm Even." if (int(sys.argv[1]) % 2) == 0 else "I'm Odd.")