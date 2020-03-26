from math  import pi, sqrt, cos, sin, acos
from numpy import around

class Euc_2D:
    def __init__(self, x = None, y = None):
        self.x = x;
        self.y = y

    def __sub__(self, other):
        return Euc_2D(self.x - other.x, self.y - other.y)

    def norm(self):
        return sqrt(self.x ** 2 + self.y ** 2)

def euc_2d_distance(city1, city2):
    return int(around((city1 - city2).norm()))

def jarak(city1, city2):
    if type(city1) != type(city2):
        print("Proses tidak berjalan, tipe koordinat berbeda")

    elif type(city1) == Euc_2D:
        return euc_2d_distance(city1, city2)

