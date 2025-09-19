num = list(map(int,input("enter numbers: ").split()))
result=[x if x<=100 else "over" for x in nums]
print(result)
