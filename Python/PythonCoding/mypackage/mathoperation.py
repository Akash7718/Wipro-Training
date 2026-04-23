"""
23-04-2026
importing user defined modules
"""
from mypackage.shape import areaofcircle, perimeterofcircle, areaofsquare, perimeterofsquare

radius = int(input('Enter Radius'))
print('Area:',areaofcircle(rad=radius))
print('peri:',perimeterofcircle(rad=radius))

si=int(input("area of square"))
print('Area:', areaofsquare(side=si))
print('peri:',perimeterofsquare(side=si))