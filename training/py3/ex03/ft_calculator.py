class calculator:
    '''Do calculations between vector and scalar'''

    def __init__(self, vec: list) -> None:
        self._vec = vec

    def __str__(self) -> str:
        return str(self._vec)

    def __add__(self, object) -> None:
        # map(lambda x: x + object, self._vec)
        self._vec = [x + object for x in self._vec]
        print(self)

    def __mul__(self, object) -> None:
        self._vec = [x * object for x in self._vec]
        print(self)

    def __sub__(self, object) -> None:
        self._vec = [x - object for x in self._vec]
        print(self)

    def __truediv__(self, object) -> None:

        def div_or_inf(x, y):
            if y == 0:
                return float('inf')
            return x / y

        self._vec = [div_or_inf(x, object) for x in self._vec]
        print(self)
