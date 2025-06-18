my_set = {"apple", "orange", "cherry"}
print(my_set)

# Duplicates Not Allowed
my_set =  {"apple", "orange", "cherry", "apple"}
print(my_set)

print(len(my_set))
print(type(my_set))

print("apple" in my_set)

my_set.add("banana")
print(my_set)

my_set.remove("cherry")
print(my_set)