# iterable: list, dictionary, tuple, set, string
# iterated --> one by one check each item in the collection

user = {
    'name' : 'Golem',
    'age' : 5006,
    'can_swim' : False
}

for item in user:
    print(item)

# dictionary methods: .items(), .values(), .keys()

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

for item in user.items():
    key, value = item
    print(key, value)

for key, value in user.items():
    print(key, value)

