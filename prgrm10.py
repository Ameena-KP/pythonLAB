color_list1=input("enter colors for list1: ").split()
color_list2=input("enter colors for list2: ").split()
print([c for c in color_list1 if c not in color_list2])

