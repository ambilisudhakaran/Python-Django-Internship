num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Choose operation(+, -, *, /): ")

if operation == "+": 
    result = num1 + num2
elif operation == "-":  
    result = num1 - num2
elif operation == "*": 
    result = num1 * num2
elif operation == "/":
    result = num1 / num2 
else: 
    result = "Invalid Operation!"
    
print("The result of this operation is:", result)
