from itertools import cycle
import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.game_over_message import GameOver


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.

    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with its segments or the other snake, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._game_over_message = ""

        

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_wall(cast)
            self._handle_game_over(cast)

    def _handle_wall(self, cast):
        """"Handles hpw the cycles interact with the walls

        Args:
            cast (Cast): The cast of Actors in the game.
        """

        cycle_one = cast.get_first_actor("cycle_one")
        cycle_two = cast.get_first_actor("cycle_two")
        cycle_one.wall(self._is_game_over)
        cycle_two.wall(self._is_game_over)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments or the other
         snake

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")
        # Adjust for two players
        # snake = cast.get_first_actor("snakes")
        cycle_one = cast.get_first_actor("cycle_one")
        cycle_two = cast.get_first_actor("cycle_two")
        # head = snake.get_segments()[0]
        cycle_one_head = cycle_one.get_cycle()
        cycle_two_head = cycle_two.get_cycle()
        # segments = snake.get_segments()[1:]
        segments_one = cycle_one.get_segments()[1:]
        segments_two = cycle_two.get_segments()[1:]
        
        # finds which user wins and displays their name

        # if cycle 2 hits cycle 1 then displays cycle 1 wins
        for segment_one in segments_one:
            if cycle_two_head.get_position().equals(segment_one.get_position()):
                score2.reduce_points()
                if score2.get_points() < 1:
                    self._game_over_message = f"{cycle_one.get_name()} wins!"
                    self._is_game_over = True
            
            # if cycle 1 hits its own tail then displays cycle 2 wins
            if cycle_one_head.get_position().equals(segment_one.get_position()):
                score1.reduce_points()
                if score1.get_points() < 1:
                    self._game_over_message = f"{cycle_two.get_name()} wins!"
                    self._is_game_over = True

        # if cycle one hits cycle 2's tail then displays cycle 2 wins
        for segment_two in segments_two:
            if cycle_one_head.get_position().equals(segment_two.get_position()):
                score1.reduce_points()
                if score2.get_points() < 1:
                    self._game_over_message = f"{cycle_two.get_name()} wins!"
                    self._is_game_over = True

            # if cycle 2 hits its own tail then displays cycle 1 wins
            if cycle_two_head.get_position().equals(segment_two.get_position()):
                score2.reduce_points()
                if score2.get_points() < 1:
                    self._game_over_message = f"{cycle_one.get_name()} wins!"
                    self._is_game_over = True

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        # gets position for gameover message
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        position = Point(x, y)
        
        if self._is_game_over:
            cycle_one = cast.get_first_actor("cycle_one")
            cycle_two = cast.get_first_actor("cycle_two")
            
            # gets segments for cycle one and two
            segments_one = cycle_one.get_segments()
            segments_two = cycle_two.get_segments()
            
            # creates gameover message
            game_over = GameOver()
            game_over.set_position(position)
            game_over.set_text(self._game_over_message)
            game_over.set_font_size(50)
            cast.add_actor("messages", game_over)
            
            #changes color of cycles to white after the game ends
            for segment in segments_one:
                segment.set_color(constants.WHITE)

            for segment in segments_two:
                segment.set_color(constants.WHITE)