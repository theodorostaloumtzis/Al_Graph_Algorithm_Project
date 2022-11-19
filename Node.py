import pygame
import GraphElement
import Colour


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
    
