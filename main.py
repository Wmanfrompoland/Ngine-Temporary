import pygame 
import numpy  as np
import renderer
from models import cube

pygame.display.set_caption("Ngine")
screen = pygame.display.set_mode((800,600))
scale = 100
center = (400,300)
angle = 0
#points,lines,fill = cube.model()

lines =[[1,2],[2,3],[3,4],[4,1],
        [5,6],[6,7],[7,8],[8,5], 
        [1,5],[2,6],[3,7],[4,8]]
points = []
points.append(np.matrix([-1, -1, 1]))
points.append(np.matrix([1, -1, 1]))
points.append(np.matrix([1,  1, 1]))
points.append(np.matrix([-1, 1, 1]))
points.append(np.matrix([-1, -1, -1]))
points.append(np.matrix([1, -1, -1]))
points.append(np.matrix([1, 1, -1]))
points.append(np.matrix([-1, 1, -1]))
fill = []
rendererObj = renderer.Renderer(screen,points,scale,center,lines,fill)

clock = pygame.time.Clock()
while True:
    angle += 0.01
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255,255,255))
    rendererObj.changeAngles(angle,angle,angle)
    rendererObj.render()
    pygame.display.update()



