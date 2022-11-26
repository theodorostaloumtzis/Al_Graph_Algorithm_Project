import pygame
import Colour
from GraphElements import GraphElement
from GraphElements import Node
from GraphElements import Edge
from random import randint

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
        return total_rows * 40
    
    elif 20 < rows <=30:
        return total_rows * 30

    elif 30 < rows <=40:
        return total_rows * 20

    elif 40 < rows <=50:
        return total_rows * 10
    else:
        return total_rows * 50

def remove_edges(graph, edges, ):
    pass







def main():
    rows = int(input("Please insert the size of the grid NxN: "))
    while rows < 3 and rows > 50:
        rows = int(input("Please enter a different size:"))

    total_rows = 2 * rows - 1

    width = ideal_width(rows)

    graph, edges = make_graph(rows, width)

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