# tuple
my_tuple = ("apple", "banana", "orange") 

print(my_tuple)
print(len(my_tuple))
print(type(my_tuple))
print(my_tuple[1])

# convert into a list, add an item and convert back into tuple
x = list(my_tuple)
x.append("kiwi")
my_tuple = tuple(x)

print(my_tuple)

# multiply tuples
fruits = ("apple", "banana", "orange")
my_tuple = fruits * 2

print(my_tuple)

