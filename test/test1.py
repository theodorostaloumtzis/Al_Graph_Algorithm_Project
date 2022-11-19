from queue import PriorityQueue
import pygame

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

#   COLOURS DEFINED
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.colour = WHITE
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.colour == RED  #returns true or false

    def is_open(self):
        return self.colour == GREEN  #returns true or false

    def is_barrier(self):
        return self.colour == BLACK  #returns true or false

    def is_start(self):
        return self.colour == ORANGE  #returns true or false

    def is_end(self):
        return self.colour == TURQUOISE  #returns true or false 

    def reset(self):
        self.colour = WHITE  

    def make_closed(self):
        self.colour = RED 

    def make_open(self):
        self.colour = GREEN

    def make_barrier(self):
        self.colour = BLACK

    def make_start(self):
        self.colour = ORANGE

    def make_end(self):
        self.colour = TURQUOISE

    def make_path(self):
        self.colour = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.width))

    def update_neighbours(self, grid):
        self.neighbours = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():    # Down node 
            self.neighbours.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():                      # Up node 
            self.neighbours.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():    # Right node 
            self.neighbours.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():                      # Left node 
            self.neighbours.append(grid[self.row][self.col - 1])

    def  __lt__(self, other):
        return False

'''#using L or Manhattan distance
def heuristicManhattan(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)'''

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()



def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = 0 #heuristicManhattan(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current) 

        if current == end:  
            reconstruct_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True

        for neighbour in current.neighbours:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score #+ heuristicManhattan(neighbour.get_pos(), end.get_pos())
                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False

#grid function
def make_grid(rows, width):
    grid = []
    total_rows = 2 * rows - 1
    gap = width // total_rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid

def draw_grid(win, rows, width):
    total_rows = 2 * rows - 1
    gap = width // total_rows
    for i in range(total_rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(total_rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
    win.fill(WHITE)
    total_rows = 2 * rows - 1
    for row in grid:
        for node in row:
            if node.row % 2 == 1 and node.col % 2 == 1:
                node.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos 

    row = y // gap
    col = x // gap

    return row, col

def main(win, width):
    ROWS = 20                    #you can change 20 width dividers of WIDTH = 800 to cahnge the amount of rows and collumns.
    TOTAL_ROWS = 2 * ROWS - 1
    grid = make_grid(ROWS, width)
    start = None
    end = None
    run = True
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]: #LEFT click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, TOTAL_ROWS, width)
                node  = grid[row][col]

                if not start and node != end:
                    start = node
                    start.make_start()

                elif not end and node != start:
                    end = node
                    end.make_end()

                elif node != end and node != start:
                    node.make_barrier()
            
            elif pygame.mouse.get_pressed()[2]: #RIGHT click  
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, TOTAL_ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbours(grid)
                        
                    algorithm(lambda: draw(win, grid, TOTAL_ROWS, width), grid, start, end) #using lamda to pass draw function as an argument to algorithm
            
                elif event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

    pygame.quit()

main(WIN, WIDTH)