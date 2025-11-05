def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

n = int(input("Enter number of terms: "))
s = 0
for i in range(1, n + 1):
    s += (i**3) / fact(i)

print("Sum =", s)
