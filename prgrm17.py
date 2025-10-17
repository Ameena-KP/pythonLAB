d = {}
n = int(input("Enter number of items: "))
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

asc = dict(sorted(d.items()))
print("Ascending order:", asc)

desc = dict(sorted(d.items(), reverse=True))
print("Descending order:", desc)
