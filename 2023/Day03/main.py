import math, re

board = list(open('input.txt'))
chars = {(row_index, col_index): [] for row_index in range(140) for col_index in range(140)
                    if board[row_index][col_index] not in '01234566789.'}


for row_index, row in enumerate(board):
    for number_match in re.finditer(r'\d+', row):
        adjacent_positions = {(adj_row, adj_col) for adj_row in (row_index - 1, row_index, row_index + 1)
                              for adj_col in range(number_match.start() - 1, number_match.end() + 1)}

        for position in adjacent_positions & chars.keys():
            chars[position].append(int(number_match.group()))

print(sum(sum(numbers) for numbers in chars.values()), sum(math.prod(numbers) for numbers in chars.values() if len(numbers) == 2))