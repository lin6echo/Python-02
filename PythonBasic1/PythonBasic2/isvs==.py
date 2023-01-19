print(True == 1)        # True
print('' == 1)          # False
print([] == 1)          # False
print(10 == 10.0)       # True
print([] == [])         # True

print(True is 1)        # False
print('' is 1)          # False
print([] is 1)          # False
print(10 is 10.0)       # False
print([] is [])         # False

a = [1,2,3]
b = [1,2,3]
print(a == b)           # True
print(a is b)           # False