# FileNotFoundError: [Errno 2] No such file or directory: 'nofile.txt'

try:
    with open("nofile.txt") as myfile:
        content = myfile.read()
except FileNotFoundError:
    print("File not found")
except:
    print("Something went wrong")