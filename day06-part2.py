import pandas as pd
with open("06input.txt", 'r') as f:
    input06 = f.read().splitlines()

grid = pd.DataFrame(0, index=range(1000), columns=range(1000))
def turn_toggle(grid, instruction):
    i = instruction.split()
    action, start, end = None, None, None
    if i[0] == "turn":
        action = i[1]
        start = list(map(int, i[2].split(',')))
        end = list(map(int, i[4].split(',')))
    elif i[0] == "toggle":
        action = "toggle"
        start = list(map(int, i[1].split(',')))
        end = list(map(int, i[3].split(',')))

    if action == "on":
        grid.loc[start[0]:end[0], start[1]:end[1]] += 1
    elif action == "off":
        grid.loc[start[0]:end[0], start[1]:end[1]] -= 1
        grid[grid < 0] = 0
    elif action == "toggle":
        grid.loc[start[0]:end[0], start[1]:end[1]] += 2

    return grid

for instruction in input06:
    grid = turn_toggle(grid, instruction)

total_lights = grid.values.sum()
print(total_lights)
