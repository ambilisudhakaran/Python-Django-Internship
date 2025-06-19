students = ["Lisa", "Rosie", "Pinky", "Alia"]

#Method 1
for name in students: 
    print(name)

print()

#Method 2
for i in range(0, len(students)):
    print(f"{i+1}. {students[i]}")

print()

#Method 3
for name in students: 
    print(f"{students.index(name) + 1}. {name}")