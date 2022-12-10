import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Powerup(Actor):

  def __init__(self):
    super().__init__()
    self._points = 0
    number = random.randint(0,1)

    if number == 1:
      self.set_text("@")
    else:
      self.set_text("#")

    self.set_color(constants.RED)
    self.reset()

  def reset(self):
    self._points = random.randint(1,8)
    x = random.randint(1, constants.COLUMNS - 1)
    y = random.randint(1, constants.ROWS - 1)
    position = Point(x, y)
    position = position.scale(constants.CELL_SIZE)
    self.set_position(position)

  def get_points(self):
    return self._points