with open("03input.txt", 'r') as f:
    directions = f.read()

    position = [(0, 0)]
    for step in directions:
        current_x, current_y = position[-1]
        if step == 'v':
            new_position = (current_x, current_y - 1)
        elif step == '^':
            new_position = (current_x, current_y + 1)
        elif step == '>':
            new_position = (current_x + 1, current_y)
        elif step == '<':
            new_position = (current_x - 1, current_y)
        position.append(new_position)

    unique_houses = len(set(position))
    print(unique_houses)