from __future__ import division
import math
import sys


def deg_to_rad(a):
    return a * math.pi / 180

def rad_to_deg(a):
    return a * 180 / math.pi

def sind(a):
    return math.sin(deg_to_rad(a))

def cosd(a):
    return math.cos(deg_to_rad(a))




class Vector3D:
    ##consructor
    def __init__(self, xx, yy, zz):
        self.x = xx
        self.y = yy
        self.z = zz

    def print_vec(self):
        print(self.x, self.y , self.z)

    def assign_val(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c
        return self

    def assign_vec(self, a):
        self.x = a.x
        self.y = a.y
        self.z = a.z

    def __eq__(self, a):
        return self.x == a.x and self.y == a.y and self.z == a.z

    def __iadd__(self, a):
        self.x += a.x
        self.y += a.y
        self.z += a.z
        return self

    def __isub__(self, a):
        self.x -= a.x
        self.y -= a.y
        self.z -= a.z
        return self

    def __imul__(self, a : float):
        self.x *= a
        self.y *= a
        self.z *= a
        return self

    def __itruediv__(self, a : float):
        self.x /= a
        self.y /= a
        self.z /= a
        return self

    def __ixor__(self, a):
        self.x *= a.x
        self.y *= a.y
        self.z *= a.z
        return self

    def __imod__(self, a):
        xx = self.x
        yy = self.y
        zz = self.z
        self.x = yy * a.z - zz * a.y
        self.y = zz * a.x - xx * a.z
        self.z = xx * a.y - yy * a.x
        return self

    def __neg__(self):
        return Vector3D(-self.x, -self.y, -self.z)

    def __add__(self, a):
        return Vector3D(self.x + a.x, self.y + a.y, self.z + a.z)

    def __sub__(self, a):
        return Vector3D(self.x - a.x, self.y - a.y, self.z - a.z)

    def __mul__(self, a):
        if isinstance(a, int) or isinstance(a, float):
            return Vector3D(self.x * a, self.y * a, self.z * a)
        else:
            return (self.x * a.x + self.y * a.y + self.z * a.z)

    def __truediv__(self, a):
        return Vector3D(self.x / a, self.y / a, self.z / a)

    def __xor__(self, a):
        return Vector3D(self.x * a.x, self.y * a.y, self.z * a.z)

    def __mod__(self, a):
        b = Vector3D(self.x, self.y, self.z)
        b %= a
        return b

    def norm(self):
        a = self.normsqr()
        return math.sqrt(a)

    def normsqr(self):
        return self * self

    def selfNormalize(self):
        a = self.norm()
        if a < sys.float_info.epsilon:
            self = Vector3D(0, 0, 0)
            return self
        else:
            self /= a
            return self

    def normalize(self):
        a = self.norm()
        if a < sys.float_info.epsilon:
            self = Vector3D(0, 0, 0)
            return self
        else:
            return self / a

    def comp(self, a):
        return self * (a.normalize())

    def self_scale(self, a):
        b = self.norm()
        if b < sys.float_info.epsilon:
            self = Vector3D(0, 0, 0)
            return self
        else:
            self *= (a / b)
            return self

    def scale(self, a):
        b = self.norm()
        if b < sys.float_info.epsilon:
            self = Vector3D(0, 0, 0)
            return self
        else:
            return self * (a/b)

    def rotateX(self, a):
        c = math.cos(a)
        s = math.sin(a)
        return self.assign_val(self.x, self.y * c - self.z * s, self.y * s + self.z * c)

    def rotateXd(self, a):
        return self.rotateX(deg_to_rad(a))

    def rotateY(self, a):
        c = math.cos(a)
        s = math.sin(a)
        return self.assign_val(self.x * c + self.z * s, self.y, -self.x * s + self.z * c)

    def rotateYd(self, a):
        return self.rotateY(deg_to_rad(a))

    def rotateZ(self, a):
        c = math.cos(a)
        s = math.sin(a)
        return self.assign_val(self.x * c - self.y * s, self.x * s + self.y * c, self.z)

    def rotateZd(self, a):
        return self.rotateZ(deg_to_rad(a))

    def reset(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def GetX(self):
        return self.x

    def GetY(self):
        return self.y

    def GetZ(self):
        return self.z

    def SetX(self, a):
        self.x = a

    def SetY(self, a):
        self.y = a

    def SetZ(self, a):
        self.z = a

    def Set_All(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c
