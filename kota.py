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

def geo_distance(city1, city2):
    (lat1,lon1) = city1.coord_tuple()
    (lat2,lon2) = city2.coord_tuple()
     
    if lat1 == lat2 and lon1 == lon2:
        return 0
    else:
        q1       = cos( lon1 - lon2 )
        q2       = cos( lat1 - lat2 )
        q3       = cos( lat1 + lat2 )
        radius   = 6378.388

        # jarak formula originates from the TSPLIB 95 documentation
        distance = radius * acos (1/2 * ((1 + q1) * q2 - (1 - q1) * q3)) + 1
        return(int(distance)) # truncate (toward zero), as per TSPLIB 95

def jarak(city1, city2):
    if type(city1) != type(city2):
        print("Can't calculate jarak between cities: different coord types")

    elif type(city1) == Euc_2D:
        return euc_2d_distance(city1, city2)

