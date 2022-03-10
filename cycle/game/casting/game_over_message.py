import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class GameOver(Actor):
    """
    Displays a Game Over Message

    Attributes:
        _points (int): The number of points the food is worth.
        set_color: Sets the font color
    """
    def __init__(self):
        """sets points to zero and sets color to green
        
        """
        super().__init__()
        self._points = 0
        self.set_color(constants.GREEN)