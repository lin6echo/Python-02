for item in 'zero to mastery':      # iterable -- string
    print(item)

for item in [1,2,3,4,5]:            # iterable -- list
    print(item)

for item in {1,2,3,4,5}:            # iterable -- set
    print(item)

for item in (1,2,3,4,5):            # iterable -- tuple
    print(item)

for item in (1,2,3,4,5):
    for x in ['a', 'b', 'c']:
        print(item, x)