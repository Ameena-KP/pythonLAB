# Lambda functions
square_area = lambda s: s * s
rectangle_area = lambda l, b: l * b
triangle_area = lambda b, h: 0.5 * b * h

# User input
side = float(input("Enter side of square: "))
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))

# Display results
print("Area of square:", square_area(side))
print("Area of rectangle:", rectangle_area(length, breadth))
print("Area of triangle:", triangle_area(base, height))
