list1 = list(map(int, input("Enter first list of integers (separated by space): ").split()))
list2 = list(map(int, input("Enter second list of integers (separated by space): ").split()))

print("\n(a) Same length:", len(list1) == len(list2))
print("(b) Same sum:", sum(list1) == sum(list2))
print("(c) Common values:", bool(set(list1) & set(list2)))
