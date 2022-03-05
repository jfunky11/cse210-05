import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color


class Cycle(Actor):
    """
    A long limbless reptile.

    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, position):
        super().__init__()

        self._segments = []
        self._color = Color(255, 255, 255)
        self._prepare_body(position)

    def get_segments(self):
        return self._segments

    def move_next(self):

        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def wall(self, number_of_segments, game):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            if not game:
                segment.set_color(self._color)
            else:
                segment.set_color(constants.WHITE)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)

    def _prepare_body(self, position):
        x = position.get_x()
        y = position.get_y()

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x, y + i * constants.CELL_SIZE)
            velocity = Point(0, 1 * -constants.CELL_SIZE)
            text = "@" if i == 0 else "#"

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(self._color)
            self._segments.append(segment)

    # def set_cycle_position(self, cycle_position):
    #     # Set the position for each cycle
    #     self._cycle_position = cycle_position
    #     for i in self._segments:
    #         # Expecting a Point class value
    #         # cycle_position = Point()
    #         cycle_y = cycle_position.get_y()
    #         cycle_x = cycle_position.get_x()
    #         i.set_position(cycle_position)
    #         cycle_position = cycle_position.add(Point(-1, 0))

    def set_body_color(self, color):
        self._color = color

        for segment in self._segments:
            segment.set_color(self._color)

