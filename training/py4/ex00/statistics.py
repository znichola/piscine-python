from math import sqrt


def ft_statistics(*args, **kwargs) -> None:
    '''
    Calculate various statistical properites
    mean, median, quartile, std, var
    '''
    def mean(ls: list[int | float]) -> float:
        '''Calculate the Mean'''
        return sum(ls) / len(ls)

    def median(ls: list[int | float]) -> int | float:
        '''Calculate the Median'''
        if len(ls) == 1:
            return ls[0]
        else:
            s = sorted(ls)
            mid = int(len(s)/2)
            return s[mid] if len(ls) % 2 else (s[mid - 1] + s[mid])/2

    def var(ls: list[int | float]) -> None:
        '''Calculate the Population Variance'''
        _mean = mean(ls)
        return mean([(x - _mean) ** 2 for x in ls])

    def std(ls: list[int | float]) -> None:
        '''Calculate the Standard Deviation'''
        return sqrt(var(ls))

    def quartile(ls: list[int | float]) -> None:
        '''Calculate Quartile (25% and 75%)'''
        if len(ls) == 1:
            return [ls[0], ls[0]]
        s = sorted(ls)
        mid = int(len(s)/2)
        m1 = mid + 1 if len(s) % 2 else mid
        return [float(median(s[:m1])), float(median(s[mid:]))]

    def do_op(op: str, ls: list[int | float]) -> None:
        if len(ls) == 0:
            print("ERROR")
        else:
            switch = {"mean": mean, "median": median,
                      "quartile": quartile, "std": std, "var": var}
            if switch.get(op):
                print(f"{op} : {switch.get(op)(ls)}")

    nums = [x for x in args if isinstance(x, int | float)]
    [do_op(kwargs[k], nums) for k in kwargs]
