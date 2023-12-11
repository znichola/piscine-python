from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):

    def set_eyes(self, eyes) -> None:
        self.eyes = eyes

    def set_hairs(self, hairs) -> None:
        self.hairs = hairs

    def get_eyes(self) -> str:
        return self.eyes

    def get_hairs(self) -> str:
        return self.hairs
