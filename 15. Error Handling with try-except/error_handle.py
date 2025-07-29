try:
    num = int(input("Enter Your Number: "))
except ValueError:
    print("Invalid Number")
else:
    print(f"You have entered {num}")