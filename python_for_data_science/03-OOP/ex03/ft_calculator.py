class calculator:
    '''Do calculations between vector and scalar'''

    def __init__(self, vec: list) -> None:
        '''Initialise the calculator class'''
        self._vec = vec

    def __str__(self) -> str:
        '''String reprisentation of class'''
        return str(self._vec)

    def __add__(self, object) -> None:
        '''Add to vector and print result'''
        self._vec = [x + object for x in self._vec]
        print(self)

    def __mul__(self, object) -> None:
        '''Multiply to vector and print result'''
        self._vec = [x * object for x in self._vec]
        print(self)

    def __sub__(self, object) -> None:
        '''Subtract to vector and print result'''
        self._vec = [x - object for x in self._vec]
        print(self)

    def __truediv__(self, object) -> None:
        '''Devide to vector and print result'''
        self._vec = [x / object if object != 0 else float('inf')
                     for x in self._vec]
        print(self)
