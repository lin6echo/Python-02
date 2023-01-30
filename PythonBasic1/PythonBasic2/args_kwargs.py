def super_func(*args):
    print(args)                 # tuple (1, 2, 3, 4, 5)
    return sum(args)

print(super_func(1,2,3,4,5))

def super_func(*args, **kwargs):
    print(kwargs)                 # dictionary {'num1': 5, 'num2': 10}
    return sum(args)

print(super_func(1,2,3,4,5, num1=5, num2=10))

def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1,2,3,4,5, num1=5, num2=10))

# Rule: params, *args, default parameters, **kwargs