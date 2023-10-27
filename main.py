import pygame 
import numpy  as np
import renderer

pygame.display.set_caption("Ngine")
screen = pygame.display.set_mode((800,600))
scale = 100
center = (400,300)
points = []
angle = 0
points.append(np.matrix([-1, -1, 1]))
points.append(np.matrix([1, -1, 1]))
points.append(np.matrix([1,  1, 1]))
points.append(np.matrix([-1, 1, 1]))
points.append(np.matrix([-1, -1, -1]))
points.append(np.matrix([1, -1, -1]))
points.append(np.matrix([1, 1, -1]))
points.append(np.matrix([-1, 1, -1]))
rendererObj = renderer.Renderer(screen,points,scale,center)

clock = pygame.time.Clock()
while True:
    angle += 0.01
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255,255,255))
    rendererObj.changeAngles(angle,angle,0)
    rendererObj.render()
    pygame.display.update()



