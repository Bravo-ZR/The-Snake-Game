from snake import Snake

class AI(Snake):
    def __init__(self, food) -> None:
        super().__init__()
        self.food = food
        self.segments[0].color("blue")

    def ai_move(self):
        food_x, food_y = self.food.position()
        snake_x, snake_y = self.head.position()

        # Calculate the horizontal and vertical distances between the snake's head and the food
        delta_x = food_x - snake_x
        delta_y = food_y - snake_y

        current_heading = self.head.heading()

        # Determine the next direction for the AI snake based on the distances
        if abs(delta_x) > abs(delta_y):
            if delta_x > 0 and current_heading != 180:
                self.right()
            elif delta_x < 0 and current_heading != 0:
                self.left()
            elif current_heading != 90:
                self.down()
            else:
                self.up()
        else:
            if delta_y > 0 and current_heading != 270:
                self.up()
            elif delta_y < 0 and current_heading != 90:
                self.down()
            elif current_heading != 180:
                self.right()
            else:
                self.left()

        if self.head.distance(self.food) < 20:
                self.food.refresh()
                self.extend()
 
        