with open("01input.txt", 'r') as f:
    instructions = f.read()

def basement_position(text):
    floor = 0
    position = 0
    for char in text:
        position += 1
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor == -1:
            return position
    return None

result = basement_position(instructions)
if result is not None:
    print(f"Basement reached at {result}")
else:
    print("Basement was never reached.")