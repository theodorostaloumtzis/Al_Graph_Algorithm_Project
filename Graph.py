import Node
import Edge
import GraphElement
import pygame
import Colour

class Graph:
    def __init__(self, graph_elements=None):
        if graph_elements is None:
            self.graph_elements = []
        else:
            self.graph_elements = graph_elements

    def add_node(self, row, col, width, total_rows, neighbours=None):
        self.nodes.append(Node(row, col, width, total_rows, neighbours))

    '''Return True if the node with the given value exists. Otherwise it returns False'''

    def find_node(self, row, col):
        pass

    '''Add a new edge between two nodes'''
    def add_edge(self, value1, value2):
        pass

    ''' Makes the graph '''
    def make_graph(self, rows, width):
        total_rows = 2 * rows - 1
        gap = width // total_rows
        for i in range(total_rows):
            self.graph_elements.append([])
            for j in range(total_rows):
                if i % 2 == 0 and j % 2 == 0:
                    self.graph_elements[i].append(Node(i, j, gap, total_rows))
                elif i % 2 == 1 and j % 2 == 1:
                    self.graph_elements.append(GraphElement(i, j , gap, total_rows))
                else:
                    self.graph_elements.append(Edge(i, j, gap, total_rows))


    ''' Draws the graph '''
    def draw_graph(self, win, rows, width):
        total_rows = 2 * rows - 1
        gap = width // total_rows
        for i in range(total_rows):
            pygame.draw.line(win, Colour.GREY, (0, i * gap), (width, i * gap))
            for j in range(total_rows):
                pygame.draw.line(win, Colour.GREY, (j * gap, 0), (j * gap, width))
