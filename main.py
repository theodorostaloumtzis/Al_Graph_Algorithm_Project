import pygame
import Colour
from GraphElements import GraphElement
from GraphElements import Node
from GraphElements import Edge
from random import randrange


'''     Makes the graph     '''
def make_graph(rows,width):
    graph = []
    edges = []
    total_rows = 2 * rows - 1
    gap = width // total_rows

    for i in range(total_rows):
        graph.append([])
        for j in range(total_rows):
            if i % 2 == 0 and j % 2 == 0:
                graph[i].append(Node(i, j, gap, total_rows))
            elif i % 2 == 1 and j % 2 == 1:
                graph[i].append(GraphElement(i, j , gap, total_rows))
            else:
                graph[i].append(Edge(i, j, gap, total_rows))
                edges.append(graph[i][j].get_value())

    return graph, edges


'''     Draws the grid     '''
def draw_grid(win, rows, width):
    total_rows = 2 * rows - 1
    gap = width // total_rows
    for i in range(total_rows):
        pygame.draw.line(win, Colour.GREY,(0, i * gap), (width, i * gap))
        for j in range(total_rows):
            pygame.draw.line(win, Colour.GREY, (j * gap, 0), (j * gap, width))


'''     Draws the window     '''
def draw(win, graph, rows, width):
    win.fill(Colour.WHITE)

    for row in graph:
        for graph_element in row:
            graph_element.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def ideal_width(rows):
    total_rows = 2 * rows - 1

    if 10 < rows <= 20:
        return total_rows * 15
    
    elif 20 < rows <=30:
        return total_rows * 13

    elif 30 < rows <=40:
        return total_rows * 10

    elif 40 < rows <=50:
        return total_rows * 7
    else:
        return total_rows * 30


def remove_edges(graph, edges, p):
    rmp = (p * len(edges))/100                          
    temp_slots = []                 #a list of random list solts used to check if ranint returned an already existing num
    rm_edges = []                   #the values of the edges to  be removed

    while len(rm_edges) < rmp:
        r = randrange(len(edges))
        if num_check(r,temp_slots):
            rm_edges.append(edges[r])
            temp_slots.append(r)
    temp = 0
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j].get_type() == "edge":
                if edge_check(graph[i][j],rm_edges):
                    graph[i][j].make_closed()
                    temp +=1

    return graph , temp_slots
        

def edge_check(edge, rm_edge):
    report = False
    for v in rm_edge:
        if v[0] == edge.row and v[1] == edge.col:
            report = True

    return report



def num_check(r,temp_slots):
    report = True
    for x in temp_slots:
        if r == x:
            report = False

    return report    


def get_valuesX(array):
    return array[0]


def get_valuesY(array):
    return array[1]


def main():
    rows = int(input("Please insert the size of the grid NxN: "))
    while rows < 3 and rows > 50:
        rows = int(input("Please enter a different size:"))

    total_rows = 2 * rows - 1
    percentage = int(input("Please insert the percentage of edges to be removed 0-100"))
    while 0 > percentage and percentage >100:
        percentage = int(input("Please insert the percentage of edges to be removed 0-100"))


    width = ideal_width(rows)

    graph, edges = make_graph(rows, width)

    graph, temp = remove_edges(graph, edges, percentage)

    
    print(len(edges))
    print(len(temp))

    win = pygame.display.set_mode((width, width))
    pygame.display.set_caption("A Path Finding Algorithm Program")

    running = True

    '''
    for i in range(total_rows):
        print()
        for j in range(total_rows):
            print(f" element:{graph[i][j].get_type()}  orientation:{graph[i][j].get_orientation()} x: {i}, y: {j}")
    '''
    

    #print(edges)
    #print(len(edges))

    while running:
        draw(win, graph, rows, width)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            

        



main()