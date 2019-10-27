from Plot import * 
import pandas as pd 
from rotations import * 
import math

def Geodetic_to_ECEF(latitude, longitude, height=0):
    #define a and b
    latitude = math.radians(latitude)
    longitude = math.radians(longitude)
    a = 6378137 #meters
    b = 6356752.31424518 #meters
    N = (a**2)/(np.sqrt(a**2*np.cos(latitude)*np.cos(latitude)+b**2*np.sin(latitude)*np.sin(latitude)))
    x = (N + height) * np.cos(latitude) * np.cos(longitude)
    y = (N + height) * np.cos(latitude) * np.sin(longitude)
    #z = ((b**2/a**2)*N + height) * np.sin(latitude)

    return x, y

"""
### Debug for geo to ecef
x1, y1, z1 = Geodetic_to_ECEF(47.0591225026
, 15.4586022146
, 405.441
)
print(x1, y1, z1)

x2, y2, z2 = Geodetic_to_ECEF(47.0591749850
, 15.4909999
, 405.441
)
print(x2, y2, z2)

print(x1-x2, y1-y2, z1-z2)

"""
