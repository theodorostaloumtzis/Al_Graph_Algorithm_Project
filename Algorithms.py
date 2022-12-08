import pygame
import Colour
from GraphElements import GraphElement
from GraphElements import Node
from GraphElements import Edge
from queue import PriorityQueue
from random import randrange


'''    Heuristic function Manhattan    '''
def h(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)


'''    Function that reconstructs the path    '''
def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		
		draw()


def algorithm_astar(draw, graph, start, end):
	count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start))
	came_from = {}
	g_score = {graph_element: float("inf") for row in graph for graph_element in row}
	g_score[start] = 0
	f_score = {graph_element: float("inf") for row in graph for graph_element in row}
	f_score[start] = h(start.get_pos(), end.get_pos())

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
			return False

		elif current.get_type() == "edge":
			for neighbour in current.neighbours:
				temp_g_score = g_score[current] + 1
				temp_f_score = temp_g_score + h(current.get_pos(), end.get_pos())
				
				if temp_f_score < f_score[neighbour]:
					came_from[neighbour] = current
					g_score[neighbour] = temp_g_score
					f_score[neighbour] = temp_g_score + h(neighbour.get_pos(), end.get_pos())

					if neighbour not in open_set_hash:
						count += 1
						open_set.put((f_score[neighbour],count,neighbour))
						open_set_hash.add(neighbour)
						neighbour.make_open()

		
		elif current.get_type() == "node": 
			for neighbour in current.neighbours:
				temp_g_score = g_score[current] + neighbour.weight
				temp_f_score = temp_g_score + h(current.get_pos(), end.get_pos())

				if temp_f_score < f_score[neighbour] :
					came_from[neighbour] = current
					g_score[neighbour] = temp_g_score
					f_score[neighbour] = temp_g_score + h(neighbour.get_pos(), end.get_pos())

					if neighbour not in open_set_hash:
						count += 1
						open_set.put((f_score[neighbour],count,neighbour))
						open_set_hash.add(neighbour)
						neighbour.make_open()

		

		draw()

		if current != start:
			current.make_closed()

	return False


def algorithm_ucs(draw, graph, start, end):
	count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start))
	came_from = {}
	g_score = {graph_element: float("inf") for row in graph for graph_element in row}
	g_score[start] = 0
	f_score = {graph_element: float("inf") for row in graph for graph_element in row}
	f_score[start] = 0

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
			return False

		elif current.get_type() == "edge":
			for neighbour in current.neighbours:
				temp_g_score = g_score[current] + 1
				
				if temp_g_score < g_score[neighbour]:
					came_from[neighbour] = current
					g_score[neighbour] = temp_g_score
					f_score[neighbour] = temp_g_score 

					if neighbour not in open_set_hash:
						count += 1
						open_set.put((f_score[neighbour],count,neighbour))
						open_set_hash.add(neighbour)
						neighbour.make_open()

		
		elif current.get_type() == "node": 
			for neighbour in current.neighbours:
				temp_g_score = g_score[current] + neighbour.weight

				if temp_g_score < g_score[neighbour]:
					came_from[neighbour] = current
					g_score[neighbour] = temp_g_score
					f_score[neighbour] = temp_g_score 

					if neighbour not in open_set_hash:
						count += 1
						open_set.put((f_score[neighbour],count,neighbour))
						open_set_hash.add(neighbour)
						neighbour.make_open()

		draw()

		if current != start:
			current.make_closed()

	return False	


def algorithm_ids(draw, graph, start, end, n):
	count = 0
	ds_count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start))
	came_from = {}
	g_score = {graph_element: float("inf") for row in graph for graph_element in row}
	g_score[start] = 0
	f_score = {graph_element: float("inf") for row in graph for graph_element in row}
	f_score[start] = 0

	open_set_hash = {start}

	while not open_set.empty() and ds_count < n:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = open_set.get()[2]
		open_set_hash.remove(current)

		if current == end:
			reconstruct_path(came_from, end, draw)
			end.make_end()
			start.make_start()
			return False

		elif current.get_type() == "edge":
			for neighbour in current.neighbours:
				temp_g_score = g_score[current] + 1
				
				if temp_g_score < g_score[neighbour]:
					came_from[neighbour] = current
					g_score[neighbour] = temp_g_score
					f_score[neighbour] = temp_g_score 

					if neighbour not in open_set_hash:
						count += 1
						open_set.put((f_score[neighbour],count,neighbour))
						open_set_hash.add(neighbour)
						neighbour.make_open()

		
		elif current.get_type() == "node": 
			for neighbour in current.neighbours:
				temp_g_score = g_score[current] + neighbour.weight

				if temp_g_score < g_score[neighbour]:
					came_from[neighbour] = current
					g_score[neighbour] = temp_g_score
					f_score[neighbour] = temp_g_score 

					if neighbour not in open_set_hash:
						count += 1
						ds_count += 1
						open_set.put((f_score[neighbour],count,neighbour))
						open_set_hash.add(neighbour)
						neighbour.make_open()

		draw()

		if current != start:
			current.make_closed()

	return False