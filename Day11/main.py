from collections import defaultdict
from itertools import combinations
import math

def parse_input():
    input =  open("test.txt").read().split('\n')
    grid = defaultdict(lambda: '.')
    
    for row_index, line_content in enumerate(input):
        for col_index, character in enumerate(line_content):
            grid[(row_index, col_index)] = character
    
    return grid

def check_col_no_galaxies(grid, colNr):
    for row, col in grid:
        if col == colNr:
            if grid[(row, col)] != '.':
                return False
    return True
 
def check_row_no_galaxies(grid, rowNr):
    for row, col in grid:
        if row == rowNr:
            if grid[(row, col)] != '.':
                return False
    return True

def insert_column(grid, colNr):
    grid_size = int(math.sqrt(len(grid.keys())))

    new_grid = defaultdict(lambda: '.')

    for (row, col), value in grid.items():
        if col >= colNr:
            new_grid[(row, col + 1)] = value
        else:
            new_grid[(row, col)] = value

    for row in range(grid_size):
        new_grid[(row, colNr)] = '.'

    return new_grid

def insert_row(grid, rowNr):
    grid_size = int(math.sqrt(len(grid.keys())))

    new_grid = defaultdict(lambda: '.')

    for (row, col), value in grid.items():
        if row >= rowNr:
            new_grid[(row + 1, col)] = value
        else:
            new_grid[(row, col)] = value

    for col in range(grid_size):
        new_grid[(rowNr, col)] = '.'

    return new_grid

def expand_universe(grid):
    colsNoGalaxies = []
    for x in range(0, int(math.sqrt(len(grid.keys())))):
        if check_col_no_galaxies(grid, x):
            colsNoGalaxies.append(x)
            
    for col in colsNoGalaxies:
        grid = insert_column(grid, col + colsNoGalaxies.index(col))

        
    rowsNoGalaxies = []
    for x in range(0, int(math.sqrt(len(grid.keys())))):
        if check_row_no_galaxies(grid, x):
            rowsNoGalaxies.append(x)

    for row in rowsNoGalaxies:
        grid = insert_row(grid, row + rowsNoGalaxies.index(row))
    
    return grid

def find_pairs(grid):
    galaxy_coords = [(row, col) for (row, col), value in grid.items() if value == '#']

    pairs = list(combinations(galaxy_coords, 2))

    return pairs

def manhattan_distance(a, b):
    b = b or tuple(0 for _ in range(len(a)))
    if len(a) != len(b):
        raise ValueError("Distance 'a' and 'b' must be the same length.")
    return sum([abs(p - q) for p, q in zip(a, b)])

def main():
    grid = expand_universe(parse_input())
    pairs = find_pairs(grid)
    total_distance = 0
    for pair in pairs:
        total_distance += manhattan_distance(pair[0], pair[1])
    
    return total_distance
        
print(main())