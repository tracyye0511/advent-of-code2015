with open("01input.txt", 'r') as f:
    instructions = f.read()

floor = 0
for char in instructions:
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1

print(floor)