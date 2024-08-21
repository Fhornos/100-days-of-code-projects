from turtle import Turtle

Initial_position = [(0, 0), (-20, 0), (-40, 0)]
INITIAL_BODY_LENGTH = 3
MAP_LIMIT = 295
MOVEMENT_SPEED = 20


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.initial_heading = 0
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in Initial_position:
            self.add_segment(position)

        for i in range(len(self.segments)):
            self.segments[i].goto(Initial_position[i])

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            coordinate = self.segments[i - 1].position()
            self.segments[i].goto(coordinate)
        self.segments[0].forward(MOVEMENT_SPEED)

    def left(self):
        self.segments[0].setheading(180)

    def up(self):
        self.segments[0].setheading(90)

    def right(self):
        self.segments[0].setheading(0)

    def down(self):
        self.segments[0].setheading(270)

    def game_over(self):
        if self.segments[0].xcor() > MAP_LIMIT or self.segments[0].xcor() < -MAP_LIMIT:
            return True
        elif self.segments[0].ycor() > MAP_LIMIT or self.segments[0].ycor() < -MAP_LIMIT:
            return True

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("green")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
