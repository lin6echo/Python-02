print(4 > 5)
print(4 < 5)
print(4 == 5)

# Python compares strings lexicographically, using the constituent characters based on their ASCII or Unicode code points. 

print('p' > 'P')            # True
print(ord('p'))             # 112
print(ord('P'))             # 80

print(1 < 2 < 3 < 4)            # True
print(1 >= 0)                   # True
print(1 <= 0)                   # False
print(0 != 0)                   # False (!= means not equal)

# logical operators ==> and, or, not also

print(not(True))                # False