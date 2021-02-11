from Graphics.rectfunction import *
from Graphics.circlefunction import *
from Graphics.Dgraphics.cuboidfunction import *
from Graphics.Dgraphics.spherefunction import *


lenght = float(input("Eneter the length: "))
width = float(input("Enter the width: "))
print("Rectangle Area =", rectarea(lenght, width))
print("Rectangle Perimeter =", rectperimeter(lenght, width))


radius = float(input("Eneter the Radius: "))
print("Circle Area =", circlearea(radius))
print("Circle Perimeter =", circleperimeter(radius))


length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
height = float(input("Enter the height: "))
print("Cuboid Area =", cuboidarea(length, width, height))
print("Cuboid Perimeter =", cuboidperimeter(length, width, height))


radius = float(input("Eneter the Radius: "))
print("Sphere Area =", spherearea(radius))
print("Sphere Perimeter =", sphereperimeter(radius))
