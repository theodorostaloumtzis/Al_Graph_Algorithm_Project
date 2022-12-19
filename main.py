import pygame
import Colour
from AlgorithmsClass import Algorithms
from GraphClass import Graph


def draw(win, graph):
    win.fill(Colour.WHITE)

    for row in graph:
        for graph_element in row:
            graph_element.draw(win)

    pygame.display.update()


def ideal_width(rows):
    total_rows = 2 * rows - 1

    if 10 < rows <= 20:
        return total_rows * 15

    elif 20 < rows <= 30:
        return total_rows * 13

    elif 30 < rows <= 40:
        return total_rows * 10

    elif 40 < rows <= 50:
        return total_rows * 7
    else:
        return total_rows * 30


def main():
    rows = int(input("Please insert the size of the grid NxN: "))
    while rows < 3 or rows > 50:
        rows = int(input("Please enter a different size:"))

    percentage = int(input("Please insert the percentage of edges to be removed 0-100: "))
    while 0 > percentage or percentage > 100:
        percentage = int(input("Please insert the percentage of edges to be removed 0-100: "))

    width = ideal_width(rows)

    graph = Graph(rows, width)

    graph.make_graph()

    graph.remove_edges(percentage)

    graph.make_random_start_end()

    win = pygame.display.set_mode((width, width))
    pygame.display.set_caption("A Path Finding Algorithm Program ")

    running = True

    while running:

        algorithm = Algorithms(graph.graph, graph.start, graph.end)
        draw(win, graph.graph)
        for row in graph.graph:
            for graph_element in row:
                graph_element.update_neighbours(graph.graph)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                graph.reset_graph()
                if event.key == pygame.K_u:
                    algorithm.algorithm_ucs(lambda: draw(win, graph.graph))

                if event.key == pygame.K_i:
                    algorithm.algorithm_ids(lambda: draw(win, graph.graph), rows * rows)

                if event.key == pygame.K_a:
                    algorithm.algorithm_astar(lambda: draw(win, graph.graph))

                if event.key == pygame.K_SPACE:
                    graph.reset_graph()

    pygame.quit()


main()
