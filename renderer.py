
import pygame 
import numpy  as np
from math import cos,sin

class Renderer:
    def __init__(self,screen,points3D,scale, center, pointsToConnect, pointsToFill):
        self.screen = screen
        self.points3D = points3D
        self.center = center
        self.scale = scale
        self.pointsToFill = pointsToFill
        self.pointsToConnect = pointsToConnect
        self.projectedPoints = [(i,i) for i in range(len(self.points3D))]
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
    
    def connectLines(self):
        for pair in self.pointsToConnect:
            start = (pair[0])-1
            end = (pair[1])-1
            #print(self.projectedPoints[end])
            pygame.draw.line(self.screen,(0,0,0),self.projectedPoints[start],self.projectedPoints[end],5)
    
    def fill(self):
        polygon = []
        polygon3D = []
        distance = 0
        for face in self.pointsToFill:
                for i in face:
                    polygon.append(self.projectedPoints[i-1])
                    polygon3D.append(self.points3D[i-1].tolist())
                distance = ((polygon3D[0][0][2]+polygon3D[1][0][2]+polygon3D[2][0][2])/3)*100
                print(distance)
                pygame.draw.polygon(self.screen, (distance,distance,distance), polygon)


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
            self.projectedPoints[i] = (x,y)
            pygame.draw.circle(self.screen, (255,0,0), (x,y), 5)
            self.connectLines()
            i += 1
    def changeAngles(self, x,y,z):
        self.angles = [x,y,z]
