def square(x: int | float) -> int | float:
    '''Square the input'''
    return x ** 2


def pow(x: int | float) -> int | float:
    '''Exponentiat the arcument, x pow x'''
    return x ** x


def outer(x: int | float, function) -> object:
    '''Number and function to return counter generator witht a static store'''
    count = 0
    last_res = x

    def inner() -> float:
        '''Counter generator with non local'''
        nonlocal count
        nonlocal last_res
        res = function(last_res)
        last_res = res
        count += 1
        return res
    return inner
