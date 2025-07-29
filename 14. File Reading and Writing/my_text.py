with open("demofile.txt", "r") as myfile:
    content = myfile.read()

print(content)

content = "Hello World!"
with open("demofile_2.txt", "w") as myfile:
    myfile.write(content)

content = "\nHello World!"
with open("demofile.txt", "a") as myfile:
    myfile.write(content)

