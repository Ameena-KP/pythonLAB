n=int(input("enter: "))
s,t=0,n
while t:
    s+=(t%10)**3
    t//=10
print("armstrong"if s==n else "not")
~                                                
