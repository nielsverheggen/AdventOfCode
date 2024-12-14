use std::collections::{HashMap, HashSet};
use utils;

fn main() {
    let grid = utils::parse_grid("day08/src/input.txt");

    let mut antennas = Vec::new();
    for (y, row) in grid.iter().enumerate() {
        for (x, &c) in row.iter().enumerate() {
            if c.is_alphanumeric() {
                antennas.push((x, y, c));
            }
        }
    }
    
    let mut antinodes: HashSet<(isize, isize)> = HashSet::new();

    for i in 0..antennas.len() {
        for j in 0..antennas.len() {
            if i == j {
                continue;
            }

            let (x1, y1, freq1) = antennas[i];
            let (x2, y2, freq2) = antennas[j];

            if freq1 != freq2 {
                continue;
            }

            let dx = x2 as isize - x1 as isize;
            let dy = y2 as isize - y1 as isize;

            let ax1 = x1 as isize - dx;
            let ay1 = y1 as isize - dy;
            let ax2 = x2 as isize + dx;
            let ay2 = y2 as isize + dy;

            if ax1 >= 0 && ax1 < grid[0].len() as isize && ay1 >= 0 && ay1 < grid.len() as isize {
                antinodes.insert((ax1, ay1));
            }
            if ax2 >= 0 && ax2 < grid[0].len() as isize && ay2 >= 0 && ay2 < grid.len() as isize {
                antinodes.insert((ax2, ay2));
            }
        }
    }

    println!("Part1: {}", antinodes.len());

    let mut freq_map: HashMap<char, Vec<(usize, usize)>> = HashMap::new();
    for &(x, y, f) in &antennas {
        freq_map.entry(f).or_default().push((x, y));
    }

    let mut antinodes_part2: HashSet<(isize, isize)> = HashSet::new();

    for (&_freq, positions) in &freq_map {
        if positions.len() == 1 {
            continue;
        }

        for i in 0..positions.len() {
            for j in (i+1)..positions.len() {
                let (x1, y1) = positions[i];
                let (x2, y2) = positions[j];

                let dx: isize = x2 as isize - x1 as isize;
                let dy: isize = y2 as isize - y1 as isize;

                let g: isize = utils::gcd(dx, dy);
                let step_x: isize = dx / g;
                let step_y: isize = dy / g;

                {
                    let mut tx: isize = x1 as isize;
                    let mut ty: isize = y1 as isize;
                    while tx >= 0 && ty >= 0 && tx < grid[0].len() as isize && ty < grid.len() as isize {
                        antinodes_part2.insert((tx, ty));

                        tx += step_x;
                        ty += step_y;
                    }
                }
                
                {
                    let mut tx: isize = x1 as isize;
                    let mut ty: isize = y1 as isize;
                    while tx >= 0 && ty >= 0 && tx < grid[0].len() as isize && ty < grid.len() as isize {
                        antinodes_part2.insert((tx, ty));

                        tx -= step_x;
                        ty -= step_y;
                    }
                }
            }
        }
    }

    println!("Part2: {}", antinodes_part2.len());
}
