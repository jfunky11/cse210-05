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

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
        self._handle_wall(cast)

    def _handle_wall(self, cast):
        snake_one = cast.get_first_actor("player_one")
        snake_two = cast.get_first_actor("player_two")
        snake_one.wall(1, self._is_game_over)
        snake_two.wall(1, self._is_game_over)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        # Adjust for two players
        # snake = cast.get_first_actor("snakes")
        player_one = cast.get_first_actor("player_one")
        player_two = cast.get_first_actor("player_two")
        # head = snake.get_segments()[0]
        player_one_head = player_one.get_segments()[0]
        player_two_head = player_two.get_segments()[0]
        # segments = snake.get_segments()[1:]
        segments_one = player_one.get_segments()[1:]
        segments_two = player_two.get_segments()[1:]

        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        position = Point(x, y)

        for segment_one in segments_one:
            if player_two_head.get_position().equals(segment_one.get_position()):
                self._is_game_over = True
                message = Actor()
                message.set_text("Player 1 Wins!")
                message.set_position(position)
                cast.add_actor("messages", message)
        for segment_two in segments_two:
            if player_one_head.get_position().equals(segment_two.get_position()):
                self._is_game_over = True
                message = Actor()
                message.set_text("Player 2 Wins!")
                message.set_position(position)
                cast.add_actor("messages", message)


        # for segment in segments:
        #     if head.get_position().equals(segment.get_position()):
        #         self._is_game_over = True

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            player_one = cast.get_first_actor("player_one")
            player_two = cast.get_first_actor("player_two")
            segments_one = player_one.get_segments()
            segments_two = player_two.get_segments()
            food = cast.get_first_actor("foods")

            for segment in segments_one:
                segment.set_color(constants.WHITE)

            for segment in segments_two:
                segment.set_color(constants.WHITE)