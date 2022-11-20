from queue import PriorityQueue
import pygame
import Colour

WIDTH = 800
HEIGHT = 500

def main(width, height):
    main_screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("A Path Finding Algorithm Program")
    main_screen.fill(Colour.WHITE)
    pygame.display.flip()
    running = True

    while running:
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                running = False
                
                
                
main(WIDTH, HEIGHT)

