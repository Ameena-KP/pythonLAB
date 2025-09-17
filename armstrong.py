num=int (input("enter a number:"))
num_str=str(num)
n=len(num_str)
armstrong=sum(int(digit)**n for digit in num_str)
if  num==armstrong:
    print num,"is an armstrong number"
else:
    print num,"is not an armstrongnumber"
