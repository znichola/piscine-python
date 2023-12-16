class calculator:
    '''Do calculations between two vectors'''

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        '''Calculate to dot product'''
        print(sum([x * y for x, y in zip(V1, V2)]))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        '''Calculate vector subtraction'''
        print([float(x + y) for x, y in zip(V1, V2)])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        '''Calculate vector addition'''
        print([float(x - y) for x, y in zip(V1, V2)])
