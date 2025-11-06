from Armstrong import is_armstrong

lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

print("Armstrong numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    if is_armstrong(num):
        print(num)
