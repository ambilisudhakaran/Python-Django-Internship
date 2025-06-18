my_list = ["yellow", "orange", "red"]

print(type(my_list)) #  type function
print(my_list) 
print(len(my_list)) # length function

if "yellow" in my_list:
    print("Yes, 'yellow' is in the colours list")

my_list[1] = "blue" # replace orange by blue
print(my_list)

my_list.append("pink") # append function
print(my_list)

my_list.remove("red") # remove function
print(my_list)

my_list.clear()
print(my_list)