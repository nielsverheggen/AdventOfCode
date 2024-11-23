input = list(map(str.split, open('input.txt')))

DIRECTIONS = {  'R': (1,0), 'D': (0,1), 'L': (-1,0), 'U': (0,-1),
                '0': (1,0), '1': (0,1), '2': (-1,0), '3': (0,-1)}

def main(steps, initial_position=0, accumulated_sum=1):
    for (step_increment, multiplier), times in steps:
        initial_position += step_increment * times
        accumulated_sum += multiplier * times * initial_position + times / 2

    return int(accumulated_sum)


def process_directions(input):
    processed_instructions = []
    for direction, step_size, _ in input:
        processed_instructions.append((DIRECTIONS[direction], int(step_size)))
    return processed_instructions

def process_codes(input):
    processed_instructions = []
    for _, _, color in input:
        processed_instructions.append((DIRECTIONS[color[7]], int(color[2:7], 16)))
    return processed_instructions

print(main(process_directions(input)))
print(main(process_codes(input)))