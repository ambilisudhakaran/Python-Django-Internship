name = input("Enter name: ")
phone = input("Enter phone: ")
contacts[name] = phone
print("Contact saved!")

# Show the contact
print("\nSaved Contacts:")
for name in contacts:
    print(name, ":", contacts[name])