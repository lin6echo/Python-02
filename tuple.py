# Tuple

my_tuple = (1,2,3,4,5)
print(my_tuple[1])
print(5 in my_tuple)

user = {
    (1,2) : [1,2,3],
    'greet' : 'hello',
    'age' : 20
}

print(user.items())     # get back the data in tuple : dict_items([((1,2), [1, 2, 3]), ('greet', 'hello'), ('age', 20)])
print(user[(1,2)])

my_tuple = (1,2,3,4,5)
new_tuple = my_tuple[1:2]

print(new_tuple)

x,y,z, *other = (1,2,3,4,5)

print(x)
print(other)

my_tuple = (1,2,3,4,5)
print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))