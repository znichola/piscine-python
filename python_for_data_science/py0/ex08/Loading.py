import sys
import os


def ft_tqdm(lst: range) -> None:
    '''show a progress bar implemented using an iterator & generator'''

    print(os.get_terminal_size())
    term = os.get_terminal_size()

    length = term.columns - 39
    total = len(lst)

    i = 1
    for item in lst:
        p = i / total
        f = int(length * p)
        b = "█" * f
        sys.stdout.write(f'\r{p:4.0%}|{b.ljust(length, " ")}| {i}/{total}')
        sys.stdout.flush()
        i += 1
        yield item

# idk what they use for the total length, but I will stick to my implementation
