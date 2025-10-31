p = float(input("principle: "))
t = float(input("time: "))
r = 12 if input("senior citizen (y/n): ").lower() == "y" else 10
print("simple interest =", (p * r * t) / 100)
