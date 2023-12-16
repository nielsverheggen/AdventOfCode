def parse_input():
    grid = {}
    with open('input.txt') as file:
        for j, row in enumerate(file):
            for i, char in enumerate(row.strip()):
                grid[complex(i, j)] = char
    return grid

def calculate_max_steps(grid, todo_list):
    steps_taken = set()
    while todo_list:
        position, dir = todo_list.pop()
        while not (position, dir) in steps_taken:
            steps_taken.add((position, dir))
            position += dir
            match grid.get(position):
                case '|': 
                    dir = 1j
                    todo_list.append((position, -dir))
                case '-': 
                    dir = -1
                    todo_list.append((position, -dir))
                case '/': 
                    dir = -complex(dir.imag, dir.real)
                case '\\': 
                    dir = complex(dir.imag, dir.real)
                case None: 
                    break
                
    return len(set(position for position, _ in steps_taken)) - 1

grid = parse_input()
def part1():
    return calculate_max_steps(grid, [(-1, 1)])

def find_max_steps(grid):
    all_directions = [1, 1j, -1, -1j]
    max_steps = 0

    for direction in all_directions:
        for position in grid:
            if position - direction not in grid:
                todo = [(position - direction, direction)]
                steps = calculate_max_steps(grid, todo)
                max_steps = max(max_steps, steps)

    return max_steps

def part2():
    return find_max_steps(grid)

print(part1())
print(part2())