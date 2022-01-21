import random

class Card:
    """ This will be able to track the points and the next card
    """

    def __init__(self) -> None:
        self.value = 0

    def roll_card(self):
        self.value = random.randint(1, 13)