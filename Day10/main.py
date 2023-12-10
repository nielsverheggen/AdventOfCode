from collections import defaultdict, deque

def read_input():
    return open("input.txt").read().split('\n')

input = read_input()
grid = defaultdict(lambda: '.')
start_position = None

for row_index, line_content in enumerate(input):
    for col_index, character in enumerate(line_content):
        grid[(row_index, col_index)] = character
        if character == 'S':
            start_position = (row_index, col_index)

def breadth_first_search(start_node, goal_node, get_neighbors):
    queue = deque()
    queue.append(start_node)
    distances = {start_node: 0} 
    parents = {}
    seen_nodes = set([start_node]) 

    while queue:
        current_node = queue.pop()

        if goal_node is not None and current_node == goal_node:
            break

        for neighbor in get_neighbors(current_node):
            if neighbor not in seen_nodes:
                seen_nodes.add(neighbor)
                parents[neighbor] = current_node
                distances[neighbor] = distances[current_node] + 1
                queue.appendleft(neighbor)

    return distances, parents, seen_nodes


def get_neighbors(cell):
    row, column = cell
    cell_char = grid[(row, column)]
    neighbors = []

    if cell_char in '|':
        if grid[(row - 1, column)] in ['|', '7', 'F']:
            neighbors.append((row - 1, column))
        if grid[(row + 1, column)] in ['|', 'J', 'L']:
            neighbors.append((row + 1, column))
    elif cell_char == '-':
        if grid[(row, column - 1)] in ['-', 'L', 'F']:
            neighbors.append((row, column - 1))
        if grid[(row, column + 1)] in ['-', '7', 'J']:
            neighbors.append((row, column + 1))
    elif cell_char == 'L':
        if grid[(row - 1, column)] in ['|', '7', 'F']:
            neighbors.append((row - 1, column))
        if grid[(row, column + 1)] in ['-', '7', 'J']:
            neighbors.append((row, column + 1))
    elif cell_char == 'J':
        if grid[(row - 1, column)] in ['|', '7', 'F']:
            neighbors.append((row - 1, column))
        if grid[(row, column - 1)] in ['-', 'L', 'F']:
            neighbors.append((row, column - 1))
    elif cell_char == '7':
        if grid[(row, column - 1)] in ['-', 'L', 'F']:
            neighbors.append((row, column - 1))
        if grid[(row + 1, column)] in ['|', 'J', 'L']:
            neighbors.append((row + 1, column))
    elif cell_char == 'F':
        if grid[(row, column + 1)] in ['-', '7', 'J']:
            neighbors.append((row, column + 1))
        if grid[(row + 1, column)] in ['|', 'J', 'L']:
            neighbors.append((row + 1, column))

    return neighbors

start_row, start_column = start_position

for symbol in ['|', '-', 'L', 'J', '7', 'F']:
    grid[start_position] = symbol
    if len(get_neighbors(start_position)) == 2:
        break

distances, _, seen_nodes = breadth_first_search(start_position, None, get_neighbors)
loop_nodes = seen_nodes
print(max(distances.values()))

def part2():
    inside_count = 0
    for row in range(len(input)):
        left_border_count = 0
        for column in range(len(input[0])):
            if (row, column) not in loop_nodes and left_border_count % 2 == 1:
                inside_count += 1
            if grid[(row, column)] in ['|', 'L', 'J'] and (row, column) in loop_nodes:
                left_border_count += 1
    
    return inside_count

print(part2())