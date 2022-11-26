import pygame
import Colour
from random import randint

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


    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.width))

    def __lt__(self, other):
	    return False





class Node(GraphElement):
    def __init__(self, row, col, width, total_rows, neighbours=None):
        super().__init__(row, col, width, total_rows)
        
        self.colour = Colour.BLACK
        self.type = "node"

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

    def is_barrier(self):
        return self.colour == Colour.BLACK

    def is_start(self):
        return self.colour == Colour.ORANGE

    def is_end(self):
        return self.colour == Colour.TURQUOISE

    def get_type(self):
        return self.type

    '''     Setters      '''
    def reset(self):
        self.colour = Colour.WHITE

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

    def update_neighbours(self, graph):
        if self.row < self.total_rows - 2 and not graph[self.row + 1][self.col].type == "empty":    #Down
          self.neighbors.append(graph[self.row + 2][self.col])  

        if self.row < self.total_rows - 2 and not graph[self.row + 1][self.col].type == "empty":    #Up
            self.neighbors.append(graph[self.row - 2][self.col])
        
        if self.row < self.total_rows - 2 and not graph[self.row + 1][self.col].type == "empty":    #Right
            self.neighbors.append(graph[self.row][self.col + 2])
        
        if self.row < self.total_rows - 2 and not graph[self.row + 1][self.col].type == "empty":    #Left
            self.neighbors.append(graph[self.row][self.col - 2])

    def __lt__(self, other):
	    return False

class Edge(GraphElement):
    def __init__(self, row, col, width, total_rows, connectors=None):
        super().__init__(row, col, width, total_rows)
        self.colour = Colour.BLACK
        self.type = "edge"
        self.weight = 0

        if  self.row % 2 == 0 and self.col % 2 == 1:
            self.orientation = "vertical"
        else: 
            self.orientation = "horizantal"
        if connectors is None:
            self.connectors = []
        else: 
            self.connectors = connectors

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
    
    '''     Setters      '''
    def reset(self):
        self.colour = Colour.WHITE

    def make_closed(self):
        self.colour = Colour.RED
    
    def make_OPEN(self):
        self.colour = Colour.GREEN

    def add_random_weight(self):
        self.weight = randint(1,20)
    
    def draw(self, win):
        if self.orientation == "vertical":
            new_x = self.x - (5 * self.width)/ 8
            new_y = self.y
            new_width = self.width / 4
            new_height = self.width
            pygame.draw().rect(win, self.colour (new_x, new_y, new_width, new_height))

        if self.orientation == "horizontal":
            new_x = self.x 
            new_y = self.y - (5 * self.width)/ 8
            new_width = self.width 
            new_height = self.width / 4
            pygame.draw().rect(win, self.colour (new_x, new_y, new_width, new_height))

    def update_connectors(self, graph):
        self.connectors = []
        if self.orientation == "vertical":
            self.connectors.append(graph[self.row - 1][self.col])  # UP Connector
            self.connectors.append(graph[self.row + 1][self.col])  # Down Connector

        if self.orintation == "horizaontal":
            self.connectors.append(graph[self.row][self.col - 1])  # LEFT Connector
            self.connectors.append(graph[self.row][self.col + 1])  # RIGHT Connector

    def __lt__(self, other):
	    return False