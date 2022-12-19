import pygame
import Colour
import Algorithms
import GraphClass

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

    graph = GraphClass

    graph.make_graph()

    graph.remove_edges(percentage)

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
                    Algorithms.algorithm_ucs(lambda: draw(win, graph.graph, rows, width), graph.graph, graph.start, graph.end)

                if event.key == pygame.K_i:
                    Algorithms.algorithm_ids(lambda: draw(win, graph.graph, rows, width), graph.graph, graph.start, graph.end, len(graph.nodes))

                if event.key == pygame.K_a:
                    Algorithms.algorithm_astar(lambda: draw(win, graph.graph, rows, width), graph.graph, graph.start, graph.end)

                if event.key == pygame.K_SPACE:
                    graph.reset_graph(graph.graph, graph.start, graph.end)

    pygame.quit()


main()
