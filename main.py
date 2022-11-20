from queue import PriorityQueue
import pygame
import Graph
import Colour

WIDTH = 800
HEIGHT = 500

def ideal_width(number):
    if 10 < number <= 20:
        return number * 40
    
    elif 20 < number <=30:
        return number * 35

    elif 30 < number <=40:
        return number * 30

    elif 40 < number <=50:
        return number * 25
    else:
        return number * 60

def main():

    ROWS = int(input("Please insert the size of the grid NxN: "))
    while ROWS < 3 and ROWS > 50:
        ROWS = int(input("Please enter a different size:"))

    total_rows = 2 * ROWS - 1

    width = ideal_width(total_rows)

    graph = Graph()
    graph.make_graph(ROWS, width)

    main_screen = pygame.display.set_mode((width, width))
    pygame.display.set_caption("A Path Finding Algorithm Program")
    main_screen.fill(Colour.WHITE)
    pygame.display.flip()
    running = True

    while running:
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                running = False
                
                
                
main()

