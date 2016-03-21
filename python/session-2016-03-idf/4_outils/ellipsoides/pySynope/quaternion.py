# coding: utf8
from __future__ import print_function
import math

def sign(a):
    if a < 0:
        return '-'
    else:
        return '+'

def hamilton_product(q1, q2):
    return [q1[0]*q2[0] - q1[1]*q2[1] - q1[2]*q2[2] - q1[3]*q2[3],
            q1[0]*q2[1] + q1[1]*q2[0] + q1[2]*q2[3] - q1[3]*q2[2],
            q1[0]*q2[2] - q1[1]*q2[3] + q1[2]*q2[0] + q1[3]*q2[1],
            q1[0]*q2[3] + q1[1]*q2[2] - q1[2]*q2[1] + q1[3]*q2[0]]

class Quaternion(object):
    def __init__(self, x=0, y=0, z=0, w=0):
        self.coords = [x, y, z]
        self.w = w

    def set_angle(self, angle, axe=[0, 0, 1]):
        self.coords = [math.sin(angle/2)*axe[0],
                       math.sin(angle/2)*axe[1],
                       math.sin(angle/2)*axe[2]]
        self.w = math.cos(angle/2)

    def rotate(self, pos):
        x, y, z = self.coords
        w = self.w
        tmp = hamilton_product([0] + pos, [w, -x, -y, -z])
        return hamilton_product([w, x, y, z], tmp)[1:]

    @property
    def x(self):
        return self.coords[0]

    @x.setter
    def x(self, value):
        self.coords[0] = value

    @property
    def y(self):
        return self.coords[1]

    @y.setter
    def y(self, value):
        self.coords[1] = value

    @property
    def z(self):
        return self.coords[2]

    @z.setter
    def z(self, value):
        self.coords[2] = value

    def __add__(self, q):
        return Quaternion(self.x + q.x,
                          self.y + q.y,
                          self.z + q.z,
                          self.w + q.w)

    def __sub__(self, q):
        return Quaternion(self.x - q.x,
                          self.y - q.y,
                          self.z - q.z,
                          self.w - q.w)

    def __mul__(self, q):
        return Quaternion(self.w*q.x + self.x*q.w + self.y*q.z - self.z*q.y,
                          self.w*q.y - self.x*q.z + self.y*q.w + self.z*q.x,
                          self.w*q.z + self.x*q.y - self.y*q.x + self.z*q.w,
                          self.w*q.w - self.x*q.x - self.y*q.y - self.z*q.z)

    def conjugate(self):
        return Quaternion(-self.x, -self.y, -self.z, self.w)

    def normalize(self):
        norm = abs(self)
        if norm == 0.:
            norm = 1.
        self.w /= norm
        self.x /= norm
        self.y /= norm
        self.z /= norm

    def __abs__(self):
        return math.sqrt(self.w*self.w + self.x*self.x + self.y*self.y + self.z*self.z);

    def __str__(self):
        s = '{} {} '.format(sign(self.w), self.w)

        for c, i in zip(self.coords, ['i', 'j', 'k']):
            s += '{} {}{} '.format(sign(c), abs(c), i)

        return s

    def __repr__(self):
        return __str__(self)

if __name__ == '__main__':  
    q = Quaternion()
    print(q)

    q.set_angle(math.pi/4)
    q.normalize()
    print(q)

    print((q*q).rotate([1, 0, 0]))
