import Node
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


class Graph:
    def __init__(self, nodes=None):
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes

    def add_node(self, row, col, width, total_rows, neighbours=None):
        self.nodes.append(Node(row, col, width, total_rows, neighbours))

    '''Return True if the node with the given value exists. Otherwise it returns False'''

    def find_node(self, row, col):
        for node in self.nodes:
            if node.col == col and node.row == row:
                return node
        return None

    '''Add a new edge between two nodes'''

    def add_edge(self, value1, value2, weight=1):
        node1 = self.find_node(value1[0], value1[1])
        node2 = self.find_node(value2[0], value2[1])

        if (node1 is not None) and (node2 is not None):
            node1.add_neighboor((node2, weight))
            node2.add_neighboor((node1, weight))

    ''' Makes the graph '''
    def make_graph(self, rows, width):
        total_rows = 2 * rows - 1
        gap = width // total_rows
        for i in range(total_rows):
            self.nodes.append([])
            for j in range(total_rows):
                if i % 2 == 0 and j % 2 == 0:
                    self.nodes[i].append(Node(i, j, gap, total_rows))

    ''' Draws the graph '''
    def draw_graph(self, win, rows, width):
        total_rows = 2 * rows - 1
        gap = width // total_rows
        for i in range(total_rows):
            pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
            for j in range(total_rows):
                pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))
