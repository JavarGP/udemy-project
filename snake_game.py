from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# by making thing in all capitals in make something a constant

class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for here_the_snake in STARTING_POSITION:
            self.add_segment(here_the_snake)

    def add_segment(self, here_the_snake):
            start_snake = Turtle(shape="square")
            start_snake.color("white")
            start_snake.penup()
            start_snake.goto(here_the_snake)
            self.segment.append(start_snake)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            # for seg_num in range(start=2, stop=0, step=-1): the for loop has key word arguments but this will cause
            # an error
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

# inheritance means a class take certain similar aspects from a largeror previously defined class
# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#
#     def breathe(self):
#         print("Inhale, exhale.")
#
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#     #this is an example of inheretence so the self parameters is replaced with the inherited class
#     def breathe(self):
#         super().breathe()
#         print("doing this underwater.")
#
#     def swim(self):
#         print("moving in water")
#
# nemo = Fish()
# nemo.swim()
# nemo.breathe()