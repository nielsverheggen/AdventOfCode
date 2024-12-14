use std::collections::BTreeMap;

use utils;

fn find_adjecent_trail_step(
    start_x: usize,
    start_y: usize,
    start_ch: char,
    grid: &BTreeMap<(usize, usize), char>,
) -> BTreeMap<(usize, usize), char> {
    let mut adjecent_trail_steps = BTreeMap::new();
    let next_ch = (start_ch as u8 + 1) as char;
    
    for ((x, y), &ch) in grid {
        let dx = *x as isize - start_x as isize;
        let dy = *y as isize - start_y as isize;


        if dx.abs() + dy.abs() == 1 && next_ch == ch {
            adjecent_trail_steps.insert((*x, *y), ch);

            for ((nx, ny), nch) in find_adjecent_trail_step(*x,  *y, ch, grid) {
                adjecent_trail_steps.insert((nx, ny), nch);
            }
        }
    }
    adjecent_trail_steps
}

fn count_trails(
    x: usize,
    y: usize,
    current_ch: char,
    grid: &BTreeMap<(usize, usize), char>,
    memo: &mut BTreeMap<(usize, usize), usize>
) -> usize {
    if current_ch == '9' {
        return 1;
    }

    if let Some(&cached) = memo.get(&(x, y)) {
        return cached;
    }

    let next_ch = ((current_ch as u8) + 1) as char;
    let mut total_paths = 0;

    for ((nx, ny), &ch) in grid {
        let dx = (*nx as isize - x as isize).abs();
        let dy = (*ny as isize - y as isize).abs();
        if dx + dy == 1 && ch == next_ch {
            total_paths += count_trails(*nx, *ny, ch, grid, memo);
        }
    }

    memo.insert((x, y), total_paths);
    total_paths
}


fn main() {
    let grid = utils::parse_grid_map("day10/src/input.txt");
    let mut total_score = 0;
    for ((x, y), &ch) in &grid {
        if ch == '0' {
            let adj_trail_steps = find_adjecent_trail_step(*x, *y, ch, &grid);
            for (_, adjch) in adj_trail_steps {
                if adjch.to_digit(10).unwrap() == 9 {
                    total_score += 1;
                }
            }
        }
    }

    println!("Part1: {}", total_score);

    let mut total_rating = 0;

    for ((x, y), &ch) in &grid {
        if ch == '0' {
            let mut memo = BTreeMap::new();
            let rating = count_trails(*x, *y, ch, &grid, &mut memo);
            total_rating += rating;
        }
    }

    println!("Part2: {}", total_rating);
}
