import numpy as np

def model():
    points = []
    points.append(np.matrix([-1, -1, 1])) 
    points.append(np.matrix([1, -1, 1]))  
    points.append(np.matrix([1, -1, -1]))
    points.append(np.matrix([-1, -1, -1])) 
    points.append(np.matrix([0, 1, 0]))

    lines = [[1,2],[2,3],[3,4],[4,1],[1,5],[2,5],[3,5],[4,5]]

    fill = [[1,2,3,4],[1,2,5],[2,3,5],[3,4,5],[4,1,5]]

    return points,lines,fill



