my_dict = {"name": "Anna", "age": 18, "city": "Germany"}

print(my_dict)
print(len(my_dict))
print(type(my_dict))

x = my_dict.keys()
print(x)

x = my_dict.values()
print(x)

x = my_dict.items()
print(x)

my_dict["hobby"] = "Painting"
print(my_dict)

my_dict.pop("city")
print(my_dict)