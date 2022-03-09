import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.cycle import Cycle



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
        position = Point(1, 0)
        self._player_name = ""
        self.set_position(position)
        self.set_text(f"{self._player_name}: {self._points}")
        #self.add_points(0)
    
    def add_points(self, points):
        """Adds the given points to the running total and updates the text.
        
        Args:
            self (Score): An instance of Score.
            points (integer): The points to add.
        """
        self._points += points
        self.set_text(f"{self._player_name}: {self._points}")
        
    def get_points(self):
        return self._points
        
    def reduce_points(self):
        self._points -= 1
        self.set_text(f"{self._player_name}: {self._points}")
        
        
    def set_player_name(self,name):
        self._player_name = name
        self.set_text(f"{self._player_name}: {self._points}")
        
    
    