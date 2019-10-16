import Vector
import random
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
        self.resolve_ball_ball(blist)

        if self.accel.norm() < 0.5:
            self.accel.Set_All(0, 0, 0)
        if self.velocity.norm() < 0.5:
            self.velocity.Set_All(0, 0, 0)

    def Draw(self):
        glColor3f(self.color.GetX(), self.color.GetY(), self.color.GetZ())
        glPushMatrix()
        glTranslated(self.center.GetX(), self.center.GetY(), self.center.GetZ())
        glutSolidSphere(self.radius, 10, 10)
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

        if self.center.GetY() - self.radius < self.bbx[2]:
            oldCenterX = self.center.GetY()
            self.center.SetY(self.bbx[2] + self.radius)
            self.velocity.SetY(-1 * self.velocity.GetY() )
            self.velocity *= collisionDumping
            self.accel *= collisionDumping

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
    
    def resolve_ball_ball(self, ball_List : list):
        # for i in ball_List:
        #     if self.detect_collision(i) == True and (self.center == i.center) == False:
        #         self.color = Vector.Vector3D(0, 0, 0)
        #         self.radius = 2
        
        for i in range(len(ball_List)):
            for j in range(len(ball_List)):
                if ball_List[i].detect_collision(ball_List[j]) == True and i != j :
                    # self.color = Vector.Vector3D(0, 0, 0)
                    # self.radius = 2
            

    def detect_collision(self, another_ball):
        other_ball_radius = another_ball.center
        if (another_ball.get_center() - self.get_center()).norm() <= (self.radius * 2) :
            return True



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
