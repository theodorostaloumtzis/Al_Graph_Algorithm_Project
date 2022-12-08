import pygame
import Colour
import Algorithms
import Graph

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

    graph, edges, nodes = Graph.make_graph(rows, width)

    graph = Graph.remove_edges(graph, edges, percentage)

    graph, start, end = Graph.random_start_end(graph)

    win = pygame.display.set_mode((width, width))
    pygame.display.set_caption("A Path Finding Algorithm Program ")

    running = True

    while running:
        draw(win, graph, rows, width)
        for row in graph:
            for graph_element in row:
                graph_element.update_neighbours(graph)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    Algorithms.algorithm_ucs(lambda: draw(win, graph, rows, width), graph, start, end)
                    pygame.event.wait()

                if event.key == pygame.K_i:
                    Algorithms.algorithm_ids(lambda: draw(win, graph, rows, width), graph, start, end, len(nodes))
                    pygame.event.wait()

                if event.key == pygame.K_a:
                    Algorithms.algorithm_astar(lambda: draw(win, graph, rows, width), graph, start, end)
                    pygame.event.wait()

                if event.key == pygame.K_SPACE:
                    graph = Graph.reset_graph(graph, start, end)

    pygame.quit()


main()
