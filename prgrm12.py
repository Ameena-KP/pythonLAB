nums = list(map(int, input("Enter numbers separated by space: ").split()))
odd_nums = [n for n in nums if n % 2 != 0]
print("List after removing even numbers:", odd_nums)

