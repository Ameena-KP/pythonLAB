# Program to generate four-digit numbers in a given range
# such that all digits are even and the number is a perfect square

import math

# Read range from user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Four-digit numbers with all even digits and perfect squares are:")

for num in range(start, end + 1):
    # Check if number is a perfect square
    root = int(math.sqrt(num))
    if root * root == num:
        # Check if all digits are even
        digits = str(num)
        if all(int(d) % 2 == 0 for d in digits):
            print(num)
