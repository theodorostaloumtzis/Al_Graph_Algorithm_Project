import pygame
import Colour


class Node:
    def __init__(self, row, col, width, total_rows, neighbours=None):
        self.row = row
        self.col = col
        self.value = [row, col]
        self.x = row * width
        self.y = col * width
        self.colour = Colour.WHITE
        if neighbours is None:
            self.neighbours = []
        else:
            self.neighbours = neighbours
        self.width = width
        self.total_rows = total_rows
        self.weight = 1

    '''      Getters      '''
    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.colour == Colour.RED

    def is_open(self):
        return self.colour == Colour.GREEN

    def is_barrier(self):
        return self.colour == Colour.BLACK

    def is_start(self):
        return self.colour == Colour.ORANGE

    def is_end(self):
        return self.colour == Colour.TURQUOISE

    def reset(self):
        self.colour = Colour.WHITE

    '''     Setters      '''
    def make_closed(self):
        self.colour = Colour.RED

    def make_open(self):
        self.colour = Colour.GREEN

    def make_barrier(self):
        self.colour = Colour.BLACK

    def make_start(self):
        self.colour = Colour.ORANGE

    def make_end(self):
        self.colour = Colour.TURQUOISE

    def make_path(self):
        self.colour = Colour.PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.width))
    
    