my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# .difference()
# .discard()
# .difference_update()
# .intersection()
# .isdisjoint()
# .issubset()
# .issuperset()
# .union()

print(my_set.difference(your_set))              # return: {1, 2, 3} show difference between two set
print(my_set)                                   # don't modify original set : {1, 2, 3, 4, 5}

my_set.discard(5)                               # remove 5 : {1, 2, 3, 4}
print(my_set)

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

my_set.difference_update(your_set)              # modify original set: {1, 2, 3}
print(my_set)

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print(my_set.intersection(your_set))            # two common things : {4, 5} don't modify the original
print(my_set & your_set) 

print(my_set.isdisjoint(your_set))              # false because has two common things 4,5

print(my_set.union(your_set))                   # return: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(my_set | your_set)

my_set = {1,2,3}
your_set = {4,5,6,7,8,9,10}

print(my_set.issubset(your_set))                # False

my_set = {4,5}
your_set = {4,5,6,7,8,9,10}

print(my_set.issubset(your_set))                # True

