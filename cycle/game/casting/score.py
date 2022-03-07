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
        #self.add_points(0)
        cycle = Cycle()
        #to get the leght of the segment list
        self._segment_count = len(cycle.get_segments())
        self.update_seg_count(self._segment_count)
        # To get the location of score from Constants file
        position = Point(constants.SCORE_X, constants.SCORE_Y)
        # to set the position of the score  
        self.set_position(position)
    
        #new methode to replace add point
    def update_seg_count(self, segment_count):
        """Adds the given points to the score's total points.
        
        Args:
            segment_count: the number of segment
        """
        self._seg_count = segment_count
         # to updated and show Segments created instead of points
        self._set_text(f"segment created: {self._seg_count} ")

        #depending on other classes, this methode will not be use 
    def add_points(self, points):
        """Adds the given points to the score's total points.

        Args:
            points (int): The points to add.
        """
        self._points += points
       
        self.set_text(f"Segments Created: {self._points}")  