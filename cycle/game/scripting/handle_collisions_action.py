from itertools import cycle
import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.

    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._game_over_message = Actor()

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
        cycle_one = cast.get_first_actor("cycle_one")
        cycle_two = cast.get_first_actor("cycle_two")
        cycle_one.wall(self._is_game_over)
        cycle_two.wall(self._is_game_over)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        # Adjust for two players
        # snake = cast.get_first_actor("snakes")
        cycle_one = cast.get_first_actor("cycle_one")
        cycle_two = cast.get_first_actor("cycle_two")
        # head = snake.get_segments()[0]
        cycle_one_head = cycle_one.get_segments()[0]
        cycle_two_head = cycle_two.get_segments()[0]
        # segments = snake.get_segments()[1:]
        segments_one = cycle_one.get_segments()[1:]
        segments_two = cycle_two.get_segments()[1:]


        
        for segment_one in segments_one:
            if cycle_two_head.get_position().equals(segment_one.get_position()):
                self._is_game_over = True
                self._game_over_message.set_text(f"{cycle_one.get_name()} wins!")

            if cycle_one_head.get_position().equals(segment_one.get_position()):
                self._is_game_over = True
                self._game_over_message.set_text(f"{cycle_two.get_name()} wins!")

        for segment_two in segments_two:
            if cycle_one_head.get_position().equals(segment_two.get_position()):
                self._is_game_over = True

                self._game_over_message.set_text(f"{cycle_two.get_name()} wins!")

            if cycle_two_head.get_position().equals(segment_two.get_position()):
                self._is_game_over = True

                self._game_over_message.set_text(f"{cycle_one.get_name()} wins!")



        # for segment in segments:
        #     if head.get_position().equals(segment.get_position()):
        #         self._is_game_over = True

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        position = Point(x, y)
        
        if self._is_game_over:
            cycle_one = cast.get_first_actor("cycle_one")
            cycle_two = cast.get_first_actor("cycle_two")
            
            segments_one = cycle_one.get_segments()
            segments_two = cycle_two.get_segments()
            
            self._game_over_message.set_font_size(45)
            self._game_over_message.set_position(position)
            self._game_over_message.set_color(constants.GREEN)
            
            cast.add_actor("messages", self._game_over_message)
            
            for segment in segments_one:
                segment.set_color(constants.WHITE)

            for segment in segments_two:
                segment.set_color(constants.WHITE)