import pygame
import Colour

class GraphElement:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.value = [row, col]
        self.x = row * width
        self.y = col * width
        self.colour = Colour.WHITE
        self.width = width
        self.total_rows = total_rows
        self.type = "empty"

    def get_pos(self):
        return self.row, self.col

    def get_type(self):
        return self.type

    def __lt__(self, other):
	    return False