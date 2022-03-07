from game.casting.actor import Actor
from game.shared.point import Point
import constants


class Score(Actor):
    """
    A record of points made or lost.

    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        self.add_points(0)
        # To get the location of score from Constants file
        position = Point(constants.SCORE_X, constants.SCORE_Y)
        # to set the position of the score  
        self.set_position(position)

    def add_points(self, points):
        """Adds the given points to the score's total points.

        Args:
            points (int): The points to add.
        """
        self._points += points
        # to updated and show Segments created instead of points
        self.set_text(f"Segments Created: {self._points}")  