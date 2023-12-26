
def ft_filter(_function, _iterable):
    '''filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.'''

    if (_function is None):
        return [i for i in _iterable if i]
    else:
        return [i for i in _iterable if _function(i)]


# print(ft_filter.__doc__)

# foo = [0, 1, -23, -9, 93, 3, 8, -0, 4, -3]
# bar = "this is a string like 43 The Other One"

# print(list(filter(lambda n: n > 0, foo)))
# print(list(filter(str.islower, bar)))


# print(ft_filter(lambda n: n > 0, foo))
# print(ft_filter(str.islower, bar))
