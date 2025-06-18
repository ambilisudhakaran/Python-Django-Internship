colors = {"red", "blue", "green", "yellow"}
print("colors :", colors)

# adding purple
colors.add("purple")
print(colors)

# removing blue
colors.remove("blue")
print(colors)

if "green" in colors:
    print("Green is in the set!")

print("The colors in the set are: ")
for color in colors:
    print(color)
