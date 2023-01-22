my_list = [1,2,3]

for item in my_list:
    print(item)
    break

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    break

for item in my_list:
    print(item)
    continue

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    continue

for item in my_list:
    pass
    print(item)
    

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    pass