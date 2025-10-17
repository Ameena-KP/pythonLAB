s=input("input a string: ")
print({ch:s.count(ch) for ch in set (s) })
