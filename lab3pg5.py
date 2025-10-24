# Program to print the multiplication table of a number

# Read number from user
n = int(input("Enter a number: "))

print(f"Multiplication table of {n}:")

# Loop from 1 to 10
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
