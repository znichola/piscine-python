from S1E9 import Character


class Baratheon(Character):
    '''A GRRM Character part of the Baratheon Family'''

    def __init__(self, first_name: str, is_alive=True) -> None:
        '''Initialise a Baratheon'''
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        return "foobar"
        # return str(list(vars(self).values()))

    def die(self) -> None:
        '''Dead the Baratheon, something bloody preferably'''
        self.is_alive = False


class Lannister(Character):
    '''A GRRM Character part of the Lannister Family'''

    def __init__(self, first_name: str, is_alive=True) -> None:
        '''Initialise a Lannister'''
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = 'blue'
        self.hairs = 'light'

    def die(self) -> None:
        '''Dead the Lannister, something bloody preferably'''
        self.is_alive = False

    def create_lannister(first_name, is_alive=True):
        '''Create a new Lannister'''
        return Lannister(first_name, is_alive)
