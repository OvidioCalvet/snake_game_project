from turtle import Turtle

STARTING_POSITIONS: list = [(0,0), (-20,0), (-40,0)]

class Snake:

    def __init__(self):
        
        self.segments = []
    
    def create_snake():

        for position in STARTING_POSITIONS:

            new_segment = Turtle()

            new_segment.shape('square')
            new_segment.color('white')
            new_segment.position(STARTING_POSITIONS[position])