from queue import PriorityQueue
import pygame
from Graph import Graph
import Colour


def ideal_width(number):
    if 10 < number <= 20:
        return number * 25
    
    elif 20 < number <=30:
        return number * 20

    elif 30 < number <=40:
        return number * 15

    elif 40 < number <=50:
        return number * 10
    else:
        return number * 40



def draw(win, graph, rows, width):
    win.fill(Colour.WHITE)

    for row in graph.graph_elements:
        for graph_element in row:
            graph_element.draw(win)

    graph.draw_graph(win, rows, width)
    pygame.display.update()


def main():

    ROWS = int(input("Please insert the size of the grid NxN: "))
    while ROWS < 3 and ROWS > 50:
        ROWS = int(input("Please enter a different size:"))

    total_rows = 2 * ROWS - 1

    width = ideal_width(total_rows)

    graph = Graph()
    graph.make_graph(ROWS, width)

    print(dir(graph))

    main_screen = pygame.display.set_mode((width, width))
    pygame.display.set_caption("A Path Finding Algorithm Program")
    
    running = True

    while running:
        draw(main_screen, graph, ROWS, width)
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                running = False


                
main()

