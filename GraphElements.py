import pygame
import Colour
from random import randrange

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
        self.orientation = "null"

    def get_pos(self):
        return self.row, self.col

    def get_type(self):
        return self.type

    def get_orientation(self):
        return self.orientation

    def get_value(self):
        return self.value[0], self.value[1]

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.width))

    def update_neighbours(self, graph):
        pass

    def __lt__(self, other):
	    return False
  

class Node(GraphElement):
    def __init__(self, row, col, width, total_rows, neighbours=None):
        super().__init__(row, col, width, total_rows)
        
        self.colour = Colour.LIGHT_GREY
        self.type = "node"
        self.orientation = "null"

        if neighbours is None:
            self.neighbours = []
        else:
            self.neighbours = neighbours

    '''      Getters      '''
    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.colour == Colour.RED

    def is_open(self):
        return self.colour == Colour.GREEN

    def is_start(self):
        return self.colour == Colour.ORANGE

    def is_end(self):
        return self.colour == Colour.TURQUOISE

    def get_type(self):
        return self.type

    def get_orientation(self):
        return self.orientation

    def get_value(self):
        v = [self.row, self.col]
        return v
    '''     Setters      '''
    def reset(self):
        self.colour = Colour.GREY

    def make_closed(self):
        self.colour = Colour.RED

    def make_open(self):
        self.colour = Colour.GREEN

    def make_start(self):
        self.colour = Colour.ORANGE

    def make_end(self):
        self.colour = Colour.BLACK

    def make_path(self):
        self.colour = Colour.PURPLE


    '''     Functions     '''
    def draw(self, win):
        pygame.draw.rect(win, Colour.BLACK, (self.x, self.y, self.width, self.width))
        new_x = self.x + 1
        new_y = self.y + 1
        new_width = self.width - 2
        pygame.draw.rect(win, self.colour, (new_x, new_y, new_width, new_width))

    def update_neighbours(self, graph):
        self.neighbours = []
        if self.row < self.total_rows - 2 and not graph[self.row + 1][self.col].is_removed():    #Down
          self.neighbours.append(graph[self.row + 1][self.col])  

        if self.row > 1 and not graph[self.row - 1][self.col].is_removed():    #Up
            self.neighbours.append(graph[self.row - 1][self.col])
        
        if self.col < self.total_rows - 2 and not graph[self.row][self.col + 1].is_removed():    #Right
            self.neighbours.append(graph[self.row][self.col + 1])
        
        if self.col > 1 and not graph[self.row][self.col - 1].is_removed():    #Left
            self.neighbours.append(graph[self.row][self.col - 1])

    def __lt__(self, other):
	    return False  


class Edge(GraphElement):
    def __init__(self, row, col, width, total_rows, neighbours=None):
        super().__init__(row, col, width, total_rows)
        self.colour = Colour.BLACK
        self.type = "edge"
        self.weight = randrange(1, 20)

        if  self.row % 2 == 0 and self.col % 2 == 1:
            self.orientation = "vertical"
        else: 
            self.orientation = "horizontal"
        if neighbours is None:
            self.neighbours = []
        else: 
            self.neighbours = neighbours


    '''      Getters      '''
    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.colour == Colour.RED

    def is_open(self):
        return self.colour == Colour.GREEN

    def is_removed(self):
        return self.colour == Colour.WHITE

    def get_type(self):
        return self.type

    def get_orientation(self):
        return self.orientation

    def get_value(self):
        v = [self.row, self.col]
        return v 

    '''     Setters      '''
    def reset(self):
        self.colour = Colour.BLACK

    def make_closed(self):
        self.colour = Colour.RED

    def make_removed(self):
        self.colour = Colour.WHITE
    
    def make_open(self):
        self.colour = Colour.GREEN
    
    def make_path(self):
        self.colour = Colour.PURPLE

    '''     Functions     '''
    def draw(self, win):
        if self.orientation == "vertical":
            pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.width))
            pygame.draw.rect(win, Colour.WHITE, (self.x, self.y, (3 *self.width)/8, self.width))
            new_x = self.x + (5 *self.width)/8
            pygame.draw.rect(win, Colour.WHITE, (new_x, self.y, ((3 *self.width)/8) + 1, self.width))

        else:
            pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.width))
            pygame.draw.rect(win, Colour.WHITE, (self.x, self.y, self.width, (3 *self.width)/8))
            new_y = self.y + (5 *self.width)/8
            pygame.draw.rect(win, Colour.WHITE, (self.x, new_y, self.width, ((3 *self.width)/8) + 1))

    
    def update_neighbours(self, graph):
        self.neighbours = []
        if self.orientation == "vertical":
            self.neighbours.append(graph[self.row][self.col - 1])  # UP Neighbour
            self.neighbours.append(graph[self.row][self.col + 1])  # Down Neighbour

        if self.orientation == "horizontal":
            self.neighbours.append(graph[self.row - 1][self.col])  # LEFT Neighbour
            self.neighbours.append(graph[self.row + 1][self.col])  # RIGHT Neighbour
 
    def __lt__(self, other):
	    return False