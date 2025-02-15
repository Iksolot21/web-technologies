import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Point(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no):
        return Point(self.y * no.z - self.z * no.y, self.z * no.x - self.x * no.z, self.x * no.y - self.y * no.x)

    def absolute(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

def plane_angle(a, b, c, d):
    AB = b - a
    BC = c - b
    CD = d - c

    X = AB.cross(BC)
    Y = BC.cross(CD)

    X_abs = X.absolute()
    Y_abs = Y.absolute()

    if X_abs == 0 or Y_abs == 0:
        return 0.0

    cos_phi = X.dot(Y) / (X_abs * Y_abs)
    cos_phi = max(min(cos_phi, 1), -1)
    phi = math.acos(cos_phi)
    return math.degrees(phi)