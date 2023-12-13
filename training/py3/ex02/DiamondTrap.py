from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):

    def __init__(self, first_name, is_alive=True):
        """Initializes the king, a cross between a Barathon and Lannister"""
        super().__init__(first_name, is_alive)
        self.eyes = "brown"  # Default values
        self.hair = "dark"

    # @property
    # def eyes(self) -> str:
    #     return self.eyes

    # @property
    # def hairs(self) -> str:
    #     return self.hairs

    # @eyes.setter
    # def eyes(self, eyes) -> None:
    #     if not isinstance(eyes, str):
    #         raise TypeError("name must be a string")
    #     self.eyes = eyes

    # @eyes.getter
    # def eyes(self) -> str:
    #     return self.eyes

    # @hairs.setter
    # def hairs(self, hairs) -> None:
    #     if not isinstance(hairs, str):
    #         raise TypeError("hair must be a string")
    #     self.hairs = hairs

    # @hairs.getter
    # def hairs(self) -> str:
    #     return self.hairs

    # def set_eyes(self, eyes) -> None:
    #     self.eyes = eyes

    # def set_hairs(self, hairs) -> None:
    #     self.hairs = hairs

    # def get_eyes(self) -> str:
    #     return self.eyes

    # def get_hairs(self) -> str:
    #     return self.hairs
