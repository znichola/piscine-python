from abc import ABC, abstractmethod


class Character(ABC):
    '''An Abstract Base class reprisenting a GRRM Character'''

    def __init__(self, first_name: str, is_alive=True) -> None:
        '''Initilise a character with a name and an optional is_alive'''
        super().__init__()
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        '''Abstract method used to dead a character'''
        pass


class Stark(Character):
    '''A GRRM Character part of the Stark Family'''

    def die(self) -> None:
        '''Dead the character, something bloody preferably'''
        self.is_alive = False


Ned = Stark("Ned")
print(Ned.__dict__)
print(Ned.is_alive)
Ned.die()
print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)
print("---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)
