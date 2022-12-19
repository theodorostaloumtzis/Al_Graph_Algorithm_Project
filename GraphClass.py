from GraphElements import GraphElement
from GraphElements import Node
from GraphElements import Edge
from random import randrange


def num_check(r, temp_slots):
    for i in temp_slots:
        if i == r:
            return False
    return True


def edge_check(edge, rm_edge):
    for v in rm_edge:
        if v[0] == edge.row and v[1] == edge.col:
            return True

    return False


class Graph:
    def __init__(self, rows, width):
        self.rows = rows
        self.width = width
        self.graph = []
        self.edges = []
        self.nodes = []
        self.total_rows = 2 * self.rows - 1
        self.gap = self.width // self.total_rows
        self.start = None
        self.end = None

    def make_graph(self):
        for i in range(self.total_rows):
            self.graph.append([])
            for j in range(self.total_rows):
                if i % 2 == 0 and j % 2 == 0:
                    self.graph[i].append(Node(i, j, self.gap, self.total_rows))
                    self.nodes.append(self.graph[i][j].get_value())
                elif i % 2 == 1 and j % 2 == 1:
                    self.graph[i].append(GraphElement(i, j, self.gap, self.total_rows))
                else:
                    self.graph[i].append(Edge(i, j, self.gap, self.total_rows))
                    self.edges.append(self.graph[i][j].get_value())

    def remove_edges(self, p):
        rmp = (p * len(self.edges)) / 100
        temp_slots = []  # a list of random list slots used to check if randint returned an already existing num
        rm_edges = []  # the values of the edges to  be removed

        while len(rm_edges) < rmp:
            r = randrange(len(self.edges))
            if num_check(r, temp_slots):
                rm_edges.append(self.edges[r])
                temp_slots.append(r)

        for i in range(len(self.graph)):
            for j in range(len(self.graph)):
                if self.graph[i][j].get_type() == "edge":
                    if edge_check(self.graph[i][j], rm_edges):
                        self.graph[i][j].make_removed()

    def make_random_start_end(self):
        tmp_x = 0
        tmp_y = 0

        while self.start is None:
            x = randrange(len(self.graph))
            y = randrange(len(self.graph))
            if self.graph[x][y].get_type() == "node":
                self.graph[x][y].make_start()
                tmp_x = x
                tmp_y = y
                self.start = self.graph[x][y]

        while self.end is None:
            x = randrange(len(self.graph))
            y = randrange(len(self.graph))
            if self.graph[x][y].get_type() == "node":
                if x != tmp_x and y != tmp_y:
                    self.graph[x][y].make_end()
                    self.end = self.graph[x][y]

    def reset_graph(self):
        for i in range(len(self.graph)):
            for j in range(len(self.graph)):

                if self.graph[i][j].get_type() == "edge" and self.graph[i][j].is_removed():
                    self.graph[i][j].make_removed()

                else:
                    self.graph[i][j].reset()

            self.graph[self.end.row][self.end.col].make_end()
            self.graph[self.start.row][self.start.col].make_start()
