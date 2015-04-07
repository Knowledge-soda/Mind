import pygame
from Mind import Orientation

pygame.init()

screen = pygame.display.set_mode((500, 500))

Map = Orientation.tiled_map("first_level")

Map.set_screen(screen)

Map.set_camera_pos(200, 200)

running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False

   screen.fill((255, 255, 255))

   Map.blit()

   pygame.display.flip()

pygame.quit()
