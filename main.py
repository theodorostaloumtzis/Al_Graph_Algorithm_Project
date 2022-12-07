import pygame
import Colour
import Algorithms
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


'''     Draws the window     '''
def draw(win, graph, rows, width):
    win.fill(Colour.WHITE)

    for row in graph:
        for graph_element in row:
            graph_element.draw(win)

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


    '''   Removes a percentage of  the edges   '''
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
                    graph[i][j].make_removed()
                    temp +=1

    return graph
        
    '''    Checks if the edge is in the for removal    '''
def edge_check(edge, rm_edge):
    report = False
    for v in rm_edge:
        if v[0] == edge.row and v[1] == edge.col:
            report = True

    return report


    '''    Checks if the random intger number exists in the list of random integers    '''
def num_check(r,temp_slots):
    report = True
    for x in temp_slots:
        if r == x:
            report = False

    return report    


    '''    Makes a random start and end    '''
def random_start_end(graph):
    x = 0
    y = 0
    temp = 0
    tmp_x = 0
    tmp_y = 0
    start = None
    end = None

    while temp != 1:
        x = randrange(len(graph))
        y = randrange(len(graph))
        if x % 2 == 0 and y % 2 == 0:
            graph[x][y].make_start()
            tmp_x = x
            tmp_y = y
            start = graph[x][y]
            temp = 1
            
    temp = 0

    while temp !=1:
        x = randrange(len(graph))
        y = randrange(len(graph))
        if x % 2 == 0 and y % 2 == 0:
            if x != tmp_x and y != tmp_y:
                graph[x][y].make_end()
                temp = 1
                end = graph[x][y]

    return graph, start, end


def choice_input(str):
    choice = int(input(str))
    while 1 > choice or choice > 4:
        choice = int(input(str))
    
    return choice


def main():
    rows = int(input("Please insert the size of the grid NxN: "))
    while rows < 3 or rows > 50:
        rows = int(input("Please enter a different size:"))

    total_rows = 2 * rows - 1
    percentage = int(input("Please insert the percentage of edges to be removed 0-100: "))
    while 0 > percentage or percentage > 100:
        percentage = int(input("Please insert the percentage of edges to be removed 0-100: "))

    width = ideal_width(rows)

    graph, edges = make_graph(rows, width)

    graph = remove_edges(graph, edges, percentage)

    graph, start, end = random_start_end(graph)

    temp_graph = graph

    win = pygame.display.set_mode((width, width))
    pygame.display.set_caption("A Path Finding Algorithm Program ")

    
    choice = choice_input("Please enter a number 1.UCS 2.IDS 3.A*:")


    running = True

    while running:
        draw(win, graph, rows, width)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if choice == 1:
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_SPACE:
                        for row in graph:
                            for graph_element in row:
                                graph_element.update_neighbours(graph)

                        Algorithms.algorithm_ucs(lambda:draw(win, graph, rows, width), graph, start, end)

                        choice = choice_input("Please enter a number 1.UCS 2.IDS 3.A* 4.reset:")

            if choice == 2:
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_SPACE:
                        for row in graph:
                            for graph_element in row:
                                graph_element.update_neighbours(graph)

                        ''' algorithm '''     

                        choice = choice_input("Please enter a number 1.UCS 2.IDS 3.A* 4.reset:")  

            if choice == 3:
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_SPACE:
                        for row in graph:
                            for graph_element in row:
                                graph_element.update_neighbours(graph)

                        Algorithms.algorithm_astar(lambda:draw(win, graph, rows, width), graph, start, end)      

                        choice = choice_input("Please enter a number 1.UCS 2.IDS 3.A* 4.reset:")   

            if choice == 4:
                graph = temp_graph  
                        

    pygame.quit()

        
main()