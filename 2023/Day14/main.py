from itertools import count
import time
start_time = time.time()
def parse_input():
    with open("input.txt") as file:
        lines = [line.strip() for line in file]
        
    board = {}
    for row_index, line in enumerate(lines):
        for column_index, character in enumerate(line):
            position = row_index + 1j * column_index
            board[position] = character
    squares = {position for position, value in board.items() if value == "#"}
    rounds = {position for position, value in board.items() if value == "O"}
    
    return board, squares, rounds

def move_rounds(rounds, direction, open_positions):
    moved_rounds = set()
    for position in rounds:
        new_position = position - direction

        if new_position in open_positions:
            moved_rounds.add(new_position)
        else:
            moved_rounds.add(position)

    return moved_rounds


def tilt(board, rounds, squares, direction=1):
    while True:
        open_positions = board.keys() - rounds - squares

        moved_rounds = move_rounds(rounds, direction, open_positions)
        
        if moved_rounds == rounds:
            return moved_rounds
        
        rounds = moved_rounds

def calculate_load(rounds):
    total_score = 0
    for position in rounds:
        vertical_position = position.real

        score = 100 - vertical_position
        total_score += score

    return int(total_score)

def part1():
    board, squares, rounds = parse_input()
    return calculate_load(tilt(board, rounds, squares))

print(part1())

def do_cycle(board, rounds, squares):
    directions = [1, 1j, -1, -1j]  # east, south, west, north

    for direction in directions:
        rounds = tilt(board, rounds, squares, direction)

    return rounds

def part2(target_cycles=1000000000):
    board, squares, rounds = parse_input()
    seen = []
    for i in count():
        rounds = do_cycle(board, rounds, squares)
        if rounds in seen:
            start = seen.index(rounds)
            break
        seen.append(rounds)
    cycle_index = (target_cycles - i) % (start - i) + i - 1
    load_value = calculate_load(seen[cycle_index])
    return load_value

print(part2())
print("--- %s seconds ---" % (time.time() - start_time))
