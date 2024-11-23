from turtle import Turtle

STARTING_POSITIONS: list = [(0,0), (-20,0), (-40,0)]

MOVE_DISTANCE: int = 20

UP: int = 90
DOWN: int = 270
LEFT: int = 180
RIGHT: int = 0

class Snake:

    def __init__(self):
        
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):

        for position in STARTING_POSITIONS:

            segment = self.new_segment()
            segment.goto(position)

    def new_segment(self):

        new_seg = Turtle('square')
        new_seg.color('white')
        new_seg.penup()
        new_seg.speed(7)
        self.segments.append(new_seg)

        return new_seg

    def move(self):

        for seg in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self): 
        
        if self.head.heading() != DOWN: self.head.setheading(UP)
    
    def down(self):

        if self.head.heading() != UP: self.head.setheading(DOWN)

    def left(self):

        if self.head.heading() != RIGHT: self.head.setheading(LEFT)

    def right(self):

        if self.head.heading() != LEFT: self.head.setheading(RIGHT)