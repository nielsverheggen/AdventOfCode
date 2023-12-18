from heapq import heappop, heappush

def parse_input():
	return [[int(cell) for cell in line] for line in open('input.txt').read().strip().split('\n')]

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def is_within_bounds(position, matrix):
    return 0 <= position[0] < len(matrix) and 0 <= position[1] < len(matrix[0])

def calculate_lightest_path(grid, min_distance, max_distance):
    priority_queue = [(0, 0, 0, -1)]
    visited = set()
    path_costs = {}

    while priority_queue:
        current_cost, current_x, current_y, previous_direction = heappop(priority_queue)

        if current_x == len(grid) - 1 and current_y == len(grid[0]) - 1:
            return current_cost

        if (current_x, current_y, previous_direction) in visited:
            continue

        visited.add((current_x, current_y, previous_direction))

        for direction_index in range(4):
            increased_cost = 0

            if direction_index == previous_direction or (direction_index + 2) % 4 == previous_direction:
                continue

            for distance in range(1, max_distance + 1):
                new_x = current_x + DIRECTIONS[direction_index][0] * distance
                new_y = current_y + DIRECTIONS[direction_index][1] * distance

                if is_within_bounds((new_x, new_y), grid):
                    increased_cost += grid[new_x][new_y]

                    if distance < min_distance:
                        continue

                    new_cost = current_cost + increased_cost

                    if path_costs.get((new_x, new_y, direction_index), float('inf')) <= new_cost:
                        continue

                    path_costs[(new_x, new_y, direction_index)] = new_cost
                    heappush(priority_queue, (new_cost, new_x, new_y, direction_index))

print(calculate_lightest_path(parse_input(), 1, 3))
print(calculate_lightest_path(parse_input(), 4, 10))
