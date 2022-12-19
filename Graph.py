from GraphElements import GraphElement
from GraphElements import Node
from GraphElements import Edge
from random import randrange

'''     Makes the graph     '''


def make_graph(rows, width):
    graph = []
    edges = []
    nodes = []
    total_rows = 2 * rows - 1
    gap = width // total_rows

    for i in range(total_rows):
        graph.append([])
        for j in range(total_rows):
            if i % 2 == 0 and j % 2 == 0:
                graph[i].append(Node(i, j, gap, total_rows))
                nodes.append(graph[i][j].get_value())
            elif i % 2 == 1 and j % 2 == 1:
                graph[i].append(GraphElement(i, j, gap, total_rows))
            else:
                graph[i].append(Edge(i, j, gap, total_rows))
                edges.append(graph[i][j].get_value())

    return graph, edges, nodes


'''   Removes a percentage of  the edges   '''


def remove_edges(graph, edges, p):
    rmp = (p * len(edges)) / 100
    temp_slots = []  # a list of random list slots used to check if randint returned an already existing num
    rm_edges = []  # the values of the edges to  be removed

    while len(rm_edges) < rmp:
        r = randrange(len(edges))
        if num_check(r, temp_slots):
            rm_edges.append(edges[r])
            temp_slots.append(r)

    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j].get_type() == "edge":
                if edge_check(graph[i][j], rm_edges):
                    graph[i][j].make_removed()

    return graph


'''    Checks if the edge is in the for removal    '''


def edge_check(edge, rm_edge):
    for v in rm_edge:
        if v[0] == edge.row and v[1] == edge.col:
            return True

    return False


'''    Checks if the random integer number exists in the list of random integers    '''


def num_check(r, temp_slots):
    for x in temp_slots:
        if r == x:
            return False

    return True


'''    Makes a random start and end    '''


def random_start_end(graph):
    temp = 0
    tmp_x = 0
    tmp_y = 0
    start = None
    end = None

    while start is None:
        x = randrange(len(graph))
        y = randrange(len(graph))
        if graph[x][y].get_type() == "node":
            graph[x][y].make_start()
            tmp_x = x
            tmp_y = y
            start = graph[x][y]

    while end is None:
        x = randrange(len(graph))
        y = randrange(len(graph))
        if graph[x][y].get_type() == "node":
            if x != tmp_x and y != tmp_y:
                graph[x][y].make_end()
                end = graph[x][y]

    return graph, start, end


'''    resets the graph starting state    '''


def reset_graph(graph, start, end):
    for i in range(len(graph)):
        for j in range(len(graph)):

            if graph[i][j].get_type() == "edge" and graph[i][j].is_removed():
                graph[i][j].make_removed()

            else:
                graph[i][j].reset()

        graph[end.row][end.col].make_end()
        graph[start.row][start.col].make_start()

    return graph
