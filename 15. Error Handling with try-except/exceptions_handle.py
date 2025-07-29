# a = 10 / 0

try:
    a = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero")
except: 
    print("Something went wrong")