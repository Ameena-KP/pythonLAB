import graphics.rectangle as rect
from graphics.circle import area as circle_area, peri as circle_peri
from graphics.graphics_3d import cube
from graphics.graphics_3d.sphere import area as sphere_area, peri as sphere_peri

# Rectangle
l = float(input("Enter length of rectangle: "))
b = float(input("Enter breadth of rectangle: "))
print("Rectangle Area:", rect.area(l, b))
print("Rectangle Perimeter:", rect.peri(l, b))

# Circle
r = float(input("\nEnter radius of circle: "))
print("Circle Area:", circle_area(r))
print("Circle Perimeter:", circle_peri(r))

# Cuboid
l = float(input("\nEnter length of cuboid: "))
b = float(input("Enter breadth of cuboid: "))
h = float(input("Enter height of cuboid: "))
print("Cuboid Area:", cube.area(l, b, h))
print("Cuboid Perimeter:", cube.peri(l, b, h))

# Sphere
r = float(input("\nEnter radius of sphere: "))
print("Sphere Area:", sphere_area(r))
print("Sphere Perimeter:", sphere_peri(r))  
