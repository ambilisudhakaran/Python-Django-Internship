sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for number in sequence:
#     print(number)

for i in range(0, len(sequence)):
    print(f"Sum of first {sequence[i]} numbers are : {sum(sequence[0:i+1])}")