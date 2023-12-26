from functools import wraps


def callLimit(limit: int):
    '''limit the number of time a function is called'''
    count = 0

    def callLimiter(function):
        '''object to return wrapped function'''

        @wraps(function)
        def limit_function(*args, **kwds):
            '''wrapped function with limiting logic'''
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
                return
        return limit_function
    return callLimiter
