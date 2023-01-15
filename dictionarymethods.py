user = {
    'basket' : [1,2,3],
    'greet' : 'hello',
    'age' : 20
}

user2 = dict(name='John')

print(user.get('age', 55))  # nem írja felül az eredetit
print(user2)

user = {
    'basket' : [1,2,3],
    'greet' : 'hello',
    'age' : 20
}

print('basket' in user)
print('size' in user.keys())
print('hello' in user.values())
print(user.items())             # return: dict_items([('basket', [1, 2, 3]), ('greet', 'hello'), ('age', 20)])

user = {
    'basket' : [1,2,3],
    'greet' : 'hello',
    'age' : 20
}

user.clear()        # return: empty dictionary
print(user)

user = {
    'basket' : [1,2,3],
    'greet' : 'hello',
    'age' : 20
}

user2 = user.copy()     # return: {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}
print(user.clear())
print(user2)

user = {
    'basket' : [1,2,3],
    'greet' : 'hello',
    'age' : 20
}

print(user.pop('age'))
print(user)                 # eltűnt az age key sor

user = {
    'basket' : [1,2,3],
    'greet' : 'hello',
    'age' : 20
}

print(user.popitem())

user = {
    'basket' : [1,2,3],
    'greet' : 'hello',
    'age' : 20
}

print(user.update({'age' : 55}))
print(user)