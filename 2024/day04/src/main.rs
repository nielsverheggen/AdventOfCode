use utils;

fn count_words(list: Vec<char>, word: &str) -> usize {
    let word_chars: Vec<char> = word.chars().collect();
    let mut count = 0;

    if list.len() < word_chars.len() {
        return 0;
    }

    for i in 0..=list.len() - word_chars.len() {
        if &list[i..i + word_chars.len()] == &word_chars[..] {
            count += 1;
        }
    }

    count
}

fn count_xmas_patterns(grid: &Vec<Vec<char>>) -> usize {
    let mut count = 0;

    for row in 1..grid.len() - 1 {
        for col in 1..grid[0].len() - 1 {
            if grid[row][col] != 'A' {
                continue;
            }

            let top_left = grid[row - 1][col - 1];
            let bottom_right = grid[row + 1][col + 1];

            let top_right = grid[row - 1][col + 1];
            let bottom_left = grid[row + 1][col - 1];

            let diag1_valid = (top_left == 'M' && bottom_right == 'S') || (top_left == 'S' && bottom_right == 'M');
            let diag2_valid = (top_right == 'M' && bottom_left == 'S') || (top_right == 'S' && bottom_left == 'M');

            if diag1_valid && diag2_valid {
                count += 1;
            }
        }
    }

    count
}


fn main() {
    let input_grid = utils::parse_grid("day04/src/input.txt");
    let row_count = input_grid.len();
    let col_count = input_grid[0].len();

    let mut total_occ = 0;

    // -
    for row in &input_grid {
        total_occ += count_words(row.clone(), "XMAS");
        total_occ += count_words(row.clone(), "SAMX");
    }

    // |
    for col in 0..col_count {
        let mut column: Vec<char> = Vec::new();
        for row in &input_grid {
            column.push(row[col]);
        }
        total_occ += count_words(column.clone(), "XMAS");
        total_occ += count_words(column.clone(), "SAMX");
    }

    // \
    for i in 0..row_count {
        let mut diagonal: Vec<char> = Vec::new();
        let mut row = i;
        let mut col = 0;
        while row < row_count && col < col_count {
            diagonal.push(input_grid[row][col]);
            row += 1;
            col += 1;
        }
        total_occ += count_words(diagonal.clone(), "XMAS");
        total_occ += count_words(diagonal.clone(), "SAMX");
    }
    for j in 1..col_count {
        let mut diagonal: Vec<char> = Vec::new();
        let mut row = 0;
        let mut col = j;
        while row < row_count && col < col_count {
            diagonal.push(input_grid[row][col]);
            row += 1;
            col += 1;
        }
        total_occ += count_words(diagonal.clone(), "XMAS");
        total_occ += count_words(diagonal.clone(), "SAMX");
    }

    // /
    for i in 0..row_count {
        let mut diagonal: Vec<char> = Vec::new();
        let mut row = i;
        let mut col = col_count - 1;
        while row < row_count && col < col_count {
            diagonal.push(input_grid[row][col]);
            row += 1;
            if col == 0 {
                break;
            } else {
                col -= 1;
            }
        }
        total_occ += count_words(diagonal.clone(), "XMAS");
        total_occ += count_words(diagonal.clone(), "SAMX");
    }
    for j in (0..col_count - 1).rev() {
        let mut diagonal: Vec<char> = Vec::new();
        let mut row = 0;
        let mut col = j;
        while row < row_count && col < col_count {
            diagonal.push(input_grid[row][col]);
            row += 1;
            if col == 0 {
                break;
            } else {
                col -= 1;
            }
        }
        total_occ += count_words(diagonal.clone(), "XMAS");
        total_occ += count_words(diagonal.clone(), "SAMX");
    }

    println!("Part1: {}", total_occ);

    println!("Part 2: {}", count_xmas_patterns(&input_grid));
}
