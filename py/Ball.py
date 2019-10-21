import Vector
import random
import math
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

damping = 0.95
collisionDumping = 0.3



class Ball:
    def __init__(self): 
        self.center = Vector.Vector3D(0, 0, 0)
        self.velocity = Vector.Vector3D(0, 0, 0)
        self.accel = Vector.Vector3D(0, 0, 0)
        self.color = Vector.Vector3D(1, 1, 1)
        self.bbx = None
        self.radius = 0
        # self.ball = None
        # self.next = None

    def print_ball(self):
        self.center.print_vec()
        self.velocity.print_vec()
        self.accel.print_vec()
        self.color.print_vec()
        print(self.bbx)

    def SetValues(self, _radius, _center, _vel, _accel, _bbx):
        self.center = _center
        self.radius = _radius
        self.velocity = _vel
        self.accel = _accel
        self.bbx = _bbx

    def SetRandomColor(self):
        self.color.SetX(random.random())
        self.color.SetY(random.random())
        self.color.SetZ(random.random())

    def IsMoving(self):
        v = self.velocity.norm()
        if v < 0.2:
            return True
        else:
            return False

    def Update(self, dt, blist):
        self.center += self.velocity * dt
        oldVelocity = self.velocity
        self.velocity += self.accel * dt
        oldAccelY = self.accel.GetY()
        oldAccelY -= 9.8
        self.accel.SetY(oldAccelY)
        self.accel *= damping

        self.ResolveCollision()
        for i in blist:
            self.resolve_ball_ball(i)

        if self.accel.norm() < 0.5:
            self.accel.Set_All(0, 0, 0)
        if self.velocity.norm() < 0.5:
            self.velocity.Set_All(0, 0, 0)
        # print(type(rt_val))
        # print(rt_val[0])
        # return myt
        # return rt_val
        # return my_t

    def Draw(self):
        glColor3f(self.color.GetX(), self.color.GetY(), self.color.GetZ())
        glPushMatrix()
        glTranslated(self.center.GetX(), self.center.GetY(), self.center.GetZ())
        glutSolidSphere(self.radius, 100, 100)
        glPopMatrix()

    def ResolveCollision(self):
        if self.center.GetX() - self.radius < self.bbx[0]:
            oldCenterX = self.center.GetX()
            self.center.SetX(self.bbx[0] + self.radius)
            self.velocity.SetX(-1 * self.velocity.GetX() )
            self.velocity *= collisionDumping
            self.accel *= collisionDumping

        if self.center.GetX() + self.radius > self.bbx[1]:
            oldCenterX = self.center.GetX()
            self.center.SetX(self.bbx[1] - self.radius)
            self.velocity.SetX(-1 * self.velocity.GetX() )
            self.velocity *= collisionDumping
            self.accel *= collisionDumping

        if self.center.GetY() - self.radius <= self.bbx[2]:
            oldCenterX = self.center.GetY()
            self.center.SetY(self.bbx[2] + self.radius)
            self.velocity.SetY(-1 * self.velocity.GetY() )
            # self.velocity *= -1
            self.velocity *= collisionDumping
            self.accel *= collisionDumping
            # if self.accel.norm() < 0.5:
            #     self.accel.Set_All(0, 0, 0)
            # if self.velocity.norm() < 0.1:
            #     self.velocity.Set_All(0, 0, 0)
            # if self.accel.GetY() < 0.5:
            #     self.accel.SetY(0)

        if self.center.GetY() + self.radius > self.bbx[3]:
            oldCenterX = self.center.GetY()
            self.center.SetY(self.bbx[3] - self.radius)
            self.velocity.SetY(-1 * self.velocity.GetY() )
            self.velocity *= collisionDumping
            self.accel *= collisionDumping
            

        if self.center.GetZ() - self.radius < self.bbx[4]:
            oldCenterX = self.center.GetZ()
            self.center.SetZ(self.bbx[4] + self.radius)
            self.velocity.SetZ(-1 * self.velocity.GetZ() )
            self.velocity *= collisionDumping
            self.accel *= collisionDumping

        if self.center.GetZ() + self.radius > self.bbx[5]:
            oldCenterX = self.center.GetZ()
            self.center.SetZ(self.bbx[5] - self.radius)
            self.velocity.SetZ(-1 * self.velocity.GetZ() )
            self.velocity *= collisionDumping
            self.accel *= collisionDumping

    def get_center(self):
        return self.center
    
    # def resolve_ball_ball(self, ball_List : list):
    #     for i in range(len(ball_List)):
    #         for j in range(len(ball_List)):
    #             if self.detect_collision(ball_two) == True and i != j :
                    

    def resolve_ball_ball(self, _another):
        if self.detect_collision(_another) and self != _another: 
            _vel_one = self.velocity
            # _vel_one.SetY(0)
            _vel_two = _another.velocity
            # _vel_two.SetY(0)
            _accel_one = self.accel
            # _accel_one.SetY(0)
            _accel_two = _another.accel
            # _accel_two.SetY(0)
            # _vel_sum = _vel_one + _vel_two
            
            # _another.velocity = _vel_one
            # _another.accel = _accel_one
            # self.velocity = _vel_two
            # self.accel = _accel_two
            # print("inside")
            
            _another.velocity = (_vel_one + _vel_two)/2
            # _another.accel = _accel_one
            self.velocity = -(_vel_one + _vel_two)/2
            # self.accel = _accel_two



    def detect_collision(self, another_ball):
        other_ball_radius = another_ball.center
        if abs((another_ball.get_center() - self.get_center()).norm()) - (self.radius * 2) <= 0.0001:
            # if self != another_ball:
            return True
        else:
            return False



class node:
    def __init__(self):
        v = Vector.Vector3D(0, 0, 0)
        b = Ball()
        self.ball = b
        self.next = None

    def getBall(self):
        return self.ball
    
    def setBall(self, a):
        self.ball = a
