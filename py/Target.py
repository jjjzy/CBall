import Ball
import Vector
import math
import random
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

class Target:
    def __init__(self):
        # self.center.Set_All(0, 10, -80)
        self.center = Vector.Vector3D(0, 10, -80)
        self.color = Vector.Vector3D(0.8, 0.7, 0.8)
        # self.color.Set_All(0.8, 0.7, 0.8)
        self.innerRadius = 0.5
        self.outerRadius = 4
        self.isMoveing = False
        self.deltaX = 0.02
        self.bbx = None

    def SetBBX(self, _bbx):
        self.bbx = _bbx

    def Update(self, a):
        if self.isMoveing is True:
            self.center.SetX(self.center.GetX() + self.deltaX)
            if self.center.GetX() < self.bbx[0]:
                self.center.SetX(self.bbx[0])
                self.deltaX *= -1
            if self.center.GetX() > self.bbx[1]:
                self.center.SetX(self.bbx[1])
                self.deltaX *= -1
        
        hit = False
        isLast = True
        for i in a:
            ballCenter = i.center
            if (ballCenter - self.center).norm() < self.outerRadius:
                if math.fabs(ballCenter.GetZ() - self.center.GetZ()) < 1.0:
                    hit = True
                    break
            
        if hit is True:
            self.isMoveing = True
            self.color.SetX(random.random())
            self.color.SetY(random.random())
            self.color.SetZ(random.random())
            self.deltaX *= 1.05
        # print("hit is ", hit)
        
    def Draw(self):
        glColor3f(self.color.GetX(),self.color.GetY(),self.color.GetZ())
        glPushMatrix()
        glTranslated(self.center.GetX(), self.center.GetY(), self.center.GetZ())
        glutSolidTorus(self.innerRadius, self.outerRadius, 20, 20)
        glPopMatrix()