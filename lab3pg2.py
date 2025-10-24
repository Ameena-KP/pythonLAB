n = int(input("Enter the number of terms: "))

# first two terms
t1 = 0
t2 = 1

if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci series up to", n, "term:")
    print(t1)
else:
    print("Fibonacci series up to", n, "terms:")
    print(t1, t2, end=" ")
    
    for i in range(2, n):
        t3 = t1 + t2
        print(t3, end=" ")
        # update values
        t1 = t2
        t2 = t3
