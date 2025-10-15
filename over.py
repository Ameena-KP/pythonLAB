numbers = input("enter integers separated by spaces: ").split()
result = []

for n in numbers:
    num = int(n)
    if num > 100:
        result.append("over")
    else:
        result.append(num)

print("Result:", result)

