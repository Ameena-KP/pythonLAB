line=input("enter a line: ")
d={w: line.split().count(w) for w in line.split()}
print(d) 
