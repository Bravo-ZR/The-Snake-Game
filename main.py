from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from _AI_ import AI
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Azure4")
screen.title("Snake")
screen.tracer(0)


#-------

snake = Snake()
food = Food()


#-----add AI------#

#ai = AI(food)

#-----add AI------#


scoreboard = Scoreboard()

#-------

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')






game_on = True
score = 0
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #-----add AI------#
    #ai.move()
    #ai.ai_move()
    #-----add AI------#
    
    #Detect Collision with food.
    if snake.head.distance(food) < 20:
        score += 1
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    #Detect Collision with wall.    
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()
        
    #Detect Tail collision    
    for segment in snake.segments[1:]:       
        if snake.head.distance(segment) < 1:
            scoreboard.reset()
            snake.reset()
            
            
screen.exitonclick()

