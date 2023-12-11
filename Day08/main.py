from itertools import cycle
from math import lcm

def parse_input(filename):
    dirSequence = ''
    nodes = {}

    with open(filename, 'r+') as file:
        directions_part, nodes_part = file.read().strip().split('\n\n')
        dirSequence = [{'L': 0, 'R': 1}[direction] for direction in directions_part]

        for raw_node in nodes_part.splitlines():
            node, left, right = raw_node[:3], raw_node[7:10], raw_node[12:15]
            nodes[node] = (left, right)
    
    return dirSequence, nodes


def move(start_node, dirSequence, nodes):
    node = start_node

    for direction in cycle(dirSequence):
        yield node
        node = nodes[node][direction]


def part1(dirSequence, nodes):
    for step, node in enumerate(move('AAA', dirSequence, nodes)):
        if node == 'ZZZ':
            return step


def part2(dirSequence, nodes):
    steps_to_finish = []

    for start_node in [node for node in nodes.keys() if node.endswith('A')]:
        for step, node in enumerate(move(start_node, dirSequence, nodes)):
            if node.endswith('Z'):
                steps_to_finish.append(step)
                break

    return lcm(*steps_to_finish)

dirSequence, nodes = parse_input('input.txt')

print(part1(dirSequence, nodes))
print(part2(dirSequence, nodes))