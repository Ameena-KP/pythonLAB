class Rectangle:
    # Method to set values
    def set_values(self, length, width):
        self.__length = length
        self.__width = width

    # Method to calculate area
    def area(self):
        return self.__length * self.__width

    # Overload '<' operator
    def __lt__(self, other):
        return self.area() < other.area()


# --- Main Program ---
r1 = Rectangle()
print("Enter details for Rectangle 1:")
l1 = float(input("Enter length: "))
w1 = float(input("Enter width: "))
r1.set_values(l1, w1)

r2 = Rectangle()
print("\nEnter details for Rectangle 2:")
l2 = float(input("Enter length: "))
w2 = float(input("Enter width: "))
r2.set_values(l2, w2)

# Compare using overloaded '<' operator
print("\nArea of Rectangle 1:", r1.area())
print("Area of Rectangle 2:", r2.area())

if r1 < r2:
    print("\nRectangle 1 is smaller than Rectangle 2.")
elif r2 < r1:
    print("\nRectangle 1 is larger than Rectangle 2.")
else:
    print("\nBoth rectangles have the same area.")

