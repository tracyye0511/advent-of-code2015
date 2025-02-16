with open("03input.txt", 'r') as f:
    directions = f.read()

    position = [(0, 0), (0, 0)]
    for i in range(len(directions)):
        current_x, current_y = position[-2]
        step = directions[i]
        if step == 'v':
            new_position = (current_x, current_y - 1)
        elif step == '^':
            new_position = (current_x, current_y + 1)
        elif step == '>':
            new_position = (current_x + 1, current_y)
        elif step == '<':
            new_position = (current_x - 1, current_y)
        position.append(new_position)

    at_least_one_present_houses = len(set(position))
    print(at_least_one_present_houses)
