class Rectangle:
    def set_values(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


# Create first rectangle
r1 = Rectangle()
print("Enter details for Rectangle 1:")
l1 = float(input("Enter length: "))
b1 = float(input("Enter breadth: "))
r1.set_values(l1, b1)

# Create second rectangle
r2 = Rectangle()
print("\nEnter details for Rectangle 2:")
l2 = float(input("Enter length: "))
b2 = float(input("Enter breadth: "))
r2.set_values(l2, b2)

# Display area and perimeter
print("\nRectangle 1 - Area:", r1.area(), " Perimeter:", r1.perimeter())
print("Rectangle 2 - Area:", r2.area(), " Perimeter:", r2.perimeter())

# Compare rectangles by area
if r1.area() > r2.area():
    print("\nRectangle 1 has a larger area.")
elif r1.area() < r2.area():
    print("\nRectangle 2 has a larger area.")
else:
    print("\nBoth rectangles have the same area.")

