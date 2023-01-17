# Set

my_set = {1,2,3,4,5,5}      # everything has to be unique
print(my_set)               # there is no duplicate :{1, 2, 3, 4, 5}

my_set.add(100)
my_set.add(2)               # already contained this data

print(my_set)

my_list = [1,2,3,4,5,5]
print(set(my_list))         # because is everything unique, 5 appear 1 time : {1, 2, 3, 4, 5}

my_set = {1,2,3,4,5,5}
#print(my_set[0])            # 'set' object does not support indexing
print(1 in my_set)
print(len(my_set))           # the only counts unique things : 5

new_set = my_set.copy()
print(new_set)