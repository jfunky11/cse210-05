import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._snake_one_direction = Point(0, -constants.CELL_SIZE)
        self._snake_two_direction = Point(0, -constants.CELL_SIZE)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.

        """

        # Snake One keyboard inputs

        # left
        if self._keyboard_service.is_key_down('a'):
            self._snake_one_direction = Point(-constants.CELL_SIZE, 0)

        # right
        if self._keyboard_service.is_key_down('d'):
            self._snake_one_direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._snake_one_direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._snake_one_direction = Point(0, constants.CELL_SIZE)

        snake_one = cast.get_first_actor("player_one")
        snake_one.turn_head(self._snake_one_direction)

        # Snake two keyboard inputs

        # left
        if self._keyboard_service.is_key_down('j'):
            self._snake_two_direction = Point(-constants.CELL_SIZE, 0)

        # right
        if self._keyboard_service.is_key_down('l'):
            self._snake_two_direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._snake_two_direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._snake_two_direction = Point(0, constants.CELL_SIZE)

        snake_two = cast.get_first_actor("player_two")
        snake_two.turn_head(self._snake_two_direction)