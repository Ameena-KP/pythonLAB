def add_numbers(*nums):
    """return the sum of all integer arguments pased to the function."""
    return sum(nums)
values = list(map(int, input("enter numbers seperated by spaces: ").split()))
print("sum =",add_numbers(*values))
