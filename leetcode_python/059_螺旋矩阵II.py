# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 02:29:19 2018

@author: Administrator
"""

class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for i in range(n)] for j in range(n)]

        
        x,y = 0, -1
        direc = self.Dir(0)
        while True:
            x, y = direc.move(matrix, x, y)
            if x == None: break
            #print ("x,y", x,y)
            pass
        
        return matrix
        
    class Dir():
        dire = 0
        
        def __init__(self, start):
            self.dire = 0 #0,right, 1, down, 2, left, 3, up
            self.row = 0 # 
            self.col = 1 
            self.dir = [[0,0,1],
                       [1,1,0],
                       [2,0,-1],
                       [3,-1,0]]
            self.route = []
            self.start = start
        
        def turn_right(self):
            self.dire, self.row, self.col = self.dir[divmod(self.dire+1, 4)[1]]
            
        def move(self, matrix, x, y):
            for _ in range(0,3):
                x1, y1 = x + self.row, y + self.col
                if not self.is_qiang(matrix, x1, y1):
                    self.route.append(matrix[x1][y1])
                    #print ("x, dire", self.route, self.dire)
                    self.start += 1
                    matrix[x1][y1] = self.start
                    #print (matrix)
                    return x1,y1 
                else:        
                    self.turn_right()
            return None, None
                    
            
        def is_qiang(self, matrix, x, y):
            if x < 0 or x >= len(matrix) or y < 0 or y >=len(matrix[0]) or matrix[x][y] != 0:
                return True
            return False

            
print (Solution().generateMatrix(3))       