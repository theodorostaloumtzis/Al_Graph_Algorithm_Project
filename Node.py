import pygame

#   COLOURS DEFINED
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Node:
    def __init__(self, row, col, width, total_rows, neighbours=None):
        self.row = row
        self.col = col
        self.value = [row, col]
        self.x = row * width
        self.y = col * width
        self.colour = WHITE
        if neighbours is None:
            self.neighbours = []
        else:
            self.neighbours = neighbours
        self.width = width
        self.total_rows = total_rows
        self.weight = 1

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.colour == RED

    def is_open(self):
        return self.colour == GREEN

    def is_barrier(self):
        return self.colour == BLACK

    def is_start(self):
        return self.colour == ORANGE

    def is_end(self):
        return self.colour == TURQUOISE

    def reset(self):
        self.colour = WHITE

    '''     Setters      '''
    def make_closed(self):
        self.colour = RED

    def make_open(self):
        self.colour = GREEN

    def make_barrier(self):
        self.colour = BLACK

    def make_start(self):
        self.colour = ORANGE

    def make_end(self):
        self.colour = TURQUOISE

    def make_path(self):
        self.colour = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.width))

    ''' Adds a new connection to the neighbour list'''
    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def update_neighbours(self, graph):
        self.neighbours = []
        if self.row < self.total_rows - 1 and not graph[self.row + 1][self.col].is_barrier():  # Down node
            self.neighbours.append(graph[self.row + 1][self.col])

        if self.row > 0 and not graph[self.row - 1][self.col].is_barrier():  # Up node
            self.neighbours.append(graph[self.row - 1][self.col])

        if self.col > 0 and not graph[self.row][self.col - 1].is_barrier():  # Left node
            self.neighbours.append(graph[self.row][self.col - 1])

        if self.col < self.total_rows - 1 and not graph[self.row][self.col + 1].is_barrier():  # Right node
            self.neighbours.append(graph[self.row][self.col + 1])

    def __lt__(self, other):
        return False
