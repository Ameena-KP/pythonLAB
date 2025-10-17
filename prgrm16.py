nums = [int(x) for x in input("Enter integers separated by spaces: ").split()]
positive_nums = [x for x in nums if x > 0]
print(positive_nums)

N = int(input("Enter N: "))
squares = [x**2 for x in range(1, N+1)]
print(squares)

word = input("Enter a word: ")
vowels = [ch for ch in word if ch.lower() in 'aeiou']
print(vowels)

ordinals = [ord(ch) for ch in word]
print(ordinals)
