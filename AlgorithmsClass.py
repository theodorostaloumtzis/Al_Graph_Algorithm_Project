import pygame
from queue import PriorityQueue


def reconstruct_path(came_from, current, draw):
    path_cost = 0
    while current in came_from:
        current = came_from[current]
        current.make_path()
        if current.get_type() == "edge":
            path_cost = path_cost + current.weight

        draw()

    return path_cost


def heuristic(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


class Algorithms:
    def __init__(self, graph, start, end):
        self.graph = graph
        self.end = end
        self.start = start
        self.count = 0
        self.open_set = PriorityQueue()
        self.open_set.put((0, self.count, self.start))
        self.come_from = {}
        self.g_score = {graph_element: float("inf") for row in graph for graph_element in row}
        self.f_score = {graph_element: float("inf") for row in graph for graph_element in row}
        self.open_set_hash = {start}

    def algorithm_astar(self, draw):
        self.g_score[self.start] = 0
        self.f_score[self.start] = heuristic(self.start.get_pos(), self.end.get_pos())
        node_count = 0

        while not self.open_set.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = self.open_set.get()[2]
            self.open_set_hash.remove(current)

            if current == self.end:
                path_cost = reconstruct_path(self.come_from, self.end, draw)
                self.end.make_end()
                self.start.make_start()
                print(f"A* Path cost: {path_cost}, Nodes expanded: {node_count}")
                return False

            elif current.get_type() == "edge":
                for neighbour in current.neighbours:
                    temp_g_score = self.g_score[current] + 1
                    temp_f_score = temp_g_score + heuristic(current.get_pos(), self.end.get_pos())

                    if temp_f_score < self.f_score[neighbour]:
                        self.come_from[neighbour] = current
                        self.g_score[neighbour] = temp_g_score
                        self.f_score[neighbour] = temp_g_score + heuristic(neighbour.get_pos(), self.end.get_pos())

                        if neighbour not in self.open_set_hash:
                            self.count += 1
                            node_count += 1
                            self.open_set.put((self.f_score[neighbour], self.count, neighbour))
                            self.open_set_hash.add(neighbour)
                            neighbour.make_open()

            elif current.get_type() == "node":
                for neighbour in current.neighbours:
                    temp_g_score = self.g_score[current] + neighbour.weight
                    temp_f_score = temp_g_score + heuristic(current.get_pos(), self.end.get_pos())

                    if temp_f_score < self.f_score[neighbour]:
                        self.come_from[neighbour] = current
                        self.g_score[neighbour] = temp_g_score
                        self.f_score[neighbour] = temp_g_score + heuristic(neighbour.get_pos(), self.end.get_pos())

                        if neighbour not in self.open_set_hash:
                            self.count += 1
                            self.open_set.put((self.f_score[neighbour], self.count, neighbour))
                            self.open_set_hash.add(neighbour)
                            neighbour.make_open()

            draw()

            if current != self.start:
                current.make_closed()

        return False

    def algorithm_ucs(self, draw):
        self.g_score[self.start] = 0
        self.f_score[self.start] = 0
        node_count = 0

        while not self.open_set.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = self.open_set.get()[2]
            self.open_set_hash.remove(current)

            if current == self.end:
                path_cost = reconstruct_path(self.come_from, self.end, draw)
                self.end.make_end()
                self.start.make_start()
                print(f"UCS Path cost: {path_cost}, Nodes expanded: {node_count}")
                return False

            elif current.get_type() == "edge":
                for neighbour in current.neighbours:
                    temp_g_score = self.g_score[current] + 1

                    if temp_g_score < self.f_score[neighbour]:
                        self.come_from[neighbour] = current
                        self.g_score[neighbour] = temp_g_score
                        self.f_score[neighbour] = temp_g_score

                        if neighbour not in self.open_set_hash:
                            self.count += 1
                            self.open_set.put((self.f_score[neighbour], self.count, neighbour))
                            self.open_set_hash.add(neighbour)
                            neighbour.make_open()

            elif current.get_type() == "node":
                for neighbour in current.neighbours:
                    temp_g_score = self.g_score[current] + neighbour.weight

                    if temp_g_score < self.f_score[neighbour]:
                        self.come_from[neighbour] = current
                        self.g_score[neighbour] = temp_g_score
                        self.f_score[neighbour] = temp_g_score

                        if neighbour not in self.open_set_hash:
                            self.count += 1
                            node_count += 1
                            self.open_set.put((self.f_score[neighbour], self.count, neighbour))
                            self.open_set_hash.add(neighbour)
                            neighbour.make_open()

            draw()

            if current != self.start:
                current.make_closed()

        return False

    def algorithm_ids(self, draw, n):
        self.g_score[self.start] = 0
        self.f_score[self.start] = 0
        ds_count = 0

        while not self.open_set.empty() and ds_count < n:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = self.open_set.get()[2]
            self.open_set_hash.remove(current)

            if current == self.end:
                path_cost = reconstruct_path(self.come_from, self.end, draw)
                self.end.make_end()
                self.start.make_start()
                print(f"IDS Path cost: {path_cost}, Nodes expanded: {ds_count}")
                return False

            elif current.get_type() == "edge":
                for neighbour in current.neighbours:
                    temp_g_score = self.g_score[current] + 1

                    if temp_g_score < self.f_score[neighbour]:
                        self.come_from[neighbour] = current
                        self.g_score[neighbour] = temp_g_score
                        self.f_score[neighbour] = temp_g_score

                        if neighbour not in self.open_set_hash:
                            self.count += 1
                            self.open_set.put((self.f_score[neighbour], self.count, neighbour))
                            self.open_set_hash.add(neighbour)
                            neighbour.make_open()

            elif current.get_type() == "node":
                for neighbour in current.neighbours:
                    temp_g_score = self.g_score[current] + neighbour.weight

                    if temp_g_score < self.f_score[neighbour]:
                        self.come_from[neighbour] = current
                        self.g_score[neighbour] = temp_g_score
                        self.f_score[neighbour] = temp_g_score

                        if neighbour not in self.open_set_hash:
                            self.count += 1
                            ds_count += 1
                            self.open_set.put((self.f_score[neighbour], self.count, neighbour))
                            self.open_set_hash.add(neighbour)
                            neighbour.make_open()

            draw()

            if ds_count >= n:
                n = ds_count + 1

            if current != self.start:
                current.make_closed()

        return False


