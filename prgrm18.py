d1 = {}
n1 = int(input("Enter number of items for first dictionary: "))
for _ in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d1[key] = value

d2 = {}
n2 = int(input("Enter number of items for second dictionary: "))
for _ in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d2[key] = value

merged = d1.copy()
merged.update(d2)
print("Merged dictionary:", merged)
