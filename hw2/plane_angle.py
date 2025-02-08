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

    if X.absolute() == 0 or Y.absolute() == 0:
        return 0.0  

    cos_phi = X.dot(Y) / (X.absolute() * Y.absolute())
    phi = math.acos(cos_phi)
    return math.degrees(phi)

if __name__ == '__main__':
    points = []
    for i in range(4):
        x, y, z = map(float, input().split())
        points.append(Point(x, y, z))

    a, b, c, d = points
    print("%.2f" % plane_angle(a, b, c, d))