s = input("enter a string: ")
new_s = s[-1] + s[1:-1] + s[0] if len(s) > 1 else s
print("result:",new_s)
