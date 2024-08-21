from time import sleep
from snake import Snake
from scoreboard import Scoreboard
import turtle
from food import Food
def main():

    # Initial Settings
    turtle.tracer(0)
    turtle.listen()
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(width=600, height=600)

    #Main
    game_on = True
    snake = Snake()
    food = Food()
    score = Scoreboard()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.down, "Down")

    while game_on:
        turtle.update()
        sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15.0:
            food.random_location()
            score.scored()
            snake.extend()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                score.game_over()
                game_on = False


        if snake.game_over():
            score.game_over()
            game_on = False

    screen.exitonclick()

if __name__ == '__main__':
    main()