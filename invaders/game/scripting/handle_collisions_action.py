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
            self._handle_powerup_collision(cast)
            self._handle_ship_collision(cast)
            self._handle_game_over(cast)

    def _handle_powerup_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        powerup = cast.get_first_actor("powerups")
        ship = cast.get_first_actor("ships")
        head = ship.get_head()

        if head.get_position().equals(powerup.get_position()):
            points = powerup.get_points()
            ship.add_shooter(points)
            score.add_points(points)
            powerup.reset()
    
    def _handle_ship_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        ship = cast.get_first_actor("ships")
        head = ship.get_head()
        enemy = enemy.get_head()
        
        for head in enemy:
            if head.get_position().equals(enemy.get_position()):
                self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            ship = cast.get_first_actor("ships")
            powerup = cast.get_first_actor("powerups")

            x = int(constants.MAX_X / 2)
            y = 0
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)