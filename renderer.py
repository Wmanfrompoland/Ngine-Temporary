import pygame 
import numpy  as np
from math import cos,sin

class Renderer:
    def __init__(self,screen,points3D,scale, center):
        self.screen = screen
        self.points3D = points3D
        self.center = center
        self.scale = scale
        self.projectedPoints = []
        self.angles = [0,0,0] # xyz

        self.projection_matrix = np.matrix([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
            ])
        
    def matrix_define(self):
            self.rotation_z = np.matrix([
            [cos(self.angles[2]), -sin(self.angles[2]), 0],
            [sin(self.angles[2]), cos(self.angles[2]), 0],
            [0, 0, 1],
            ])

            self.rotation_y = np.matrix([
            [cos(self.angles[1]), 0, sin(self.angles[1])],
            [0, 1, 0],
            [-sin(self.angles[1]), 0, cos(self.angles[1])],
            ])

            self.rotation_x = np.matrix([
            [1, 0, 0],
            [0, cos(self.angles[0]), -sin(self.angles[0])],
            [0, sin(self.angles[0]), cos(self.angles[0])],
            ])
    


    def render(self):
        i = 0
        self.matrix_define()
        for point in self.points3D:
            rotated2d = np.dot(self.rotation_z, point.reshape((3,1)))
            rotated2d = np.dot(self.rotation_y, rotated2d)
            rotated2d = np.dot(self.rotation_x, rotated2d)
            projected2d = np.dot(self.projection_matrix, rotated2d)

            x = int(projected2d[0][0] * self.scale) + self.center[0]
            y = int(projected2d[1][0] * self.scale) + self.center[1]
            self.projectedPoints.append([])
            self.projectedPoints[i] = [x,y]
            pygame.draw.circle(self.screen, (255,0,0), (x,y), 5)
            i += 1
    def changeAngles(self, x,y,z):
        self.angles = [x,y,z]
