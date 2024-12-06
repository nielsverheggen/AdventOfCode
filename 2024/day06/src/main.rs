use utils;

#[derive(Copy, Clone, Debug, PartialEq, Eq)]
enum Direction {
    Up,
    Right,
    Down,
    Left,
}

impl Direction {
    fn turn_right(self) -> Self {
        match self {
            Direction::Up => Direction::Right,
            Direction::Right => Direction::Down,
            Direction::Down => Direction::Left,
            Direction::Left => Direction::Up,
        }
    }

    fn delta(self) -> (isize, isize) {
        match self {
            Direction::Up => (0, -1),
            Direction::Right => (1, 0),
            Direction::Down => (0, 1),
            Direction::Left => (-1, 0),
        }
    }

    fn from_char(c: char) -> Option<Direction> {
        match c {
            '^' => Some(Direction::Up),
            '>' => Some(Direction::Right),
            'v' => Some(Direction::Down),
            '<' => Some(Direction::Left),
            _ => None,
        }
    }
}

#[derive(Copy, Clone, Debug)]
struct State {
    x: usize,
    y: usize,
    d: Direction,
}


fn main() {
    let input_lines = utils::parse_lines("day06/src/input.txt");

    let mut grid: Vec<Vec<char>> = Vec::new();
    for line in input_lines {
        grid.push(line.chars().collect());
    }

    let height = grid.len();
    let width = grid.first().map(|row| row.len()).unwrap_or(0);

    let mut start_state: Option<State> = None;
    for (y, row) in grid.iter().enumerate() {
        for (x, &c) in row.iter().enumerate() {
            if let Some(d) = Direction::from_char(c) {
                start_state = Some(State { x, y, d });
                break;
            }
        }
        if start_state.is_some() {
            break;
        }
    }

    let start_state = start_state.expect("No starting position found in the input.");

    let dir_to_index = |d: Direction| match d {
        Direction::Up => 0,
        Direction::Right => 1,
        Direction::Down => 2,
        Direction::Left => 3,
    };

    let mut next_state_table: Vec<Vec<[Option<State>; 4]>> = vec![vec![[None; 4]; width]; height];

    for y in 0..height {
        for x in 0..width {
            if grid[y][x] == '#' {
                for d_i in 0..4 {
                    next_state_table[y][x][d_i] = None;
                }
                continue;
            }

            for d_i in 0..4 {
                let d = match d_i {
                    0 => Direction::Up,
                    1 => Direction::Right,
                    2 => Direction::Down,
                    3 => Direction::Left,
                    _ => unreachable!(),
                };

                let (dx, dy) = d.delta();
                let nx = x as isize + dx;
                let ny = y as isize + dy;

                if nx < 0 || ny < 0 || nx >= width as isize || ny >= height as isize {
                    next_state_table[y][x][d_i] = None;
                } else {
                    let nxu = nx as usize;
                    let nyu = ny as usize;
                    if grid[nyu][nxu] == '#' {
                        let new_dir = d.turn_right();
                        next_state_table[y][x][d_i] = Some(State { x, y, d: new_dir });
                    } else {
                        next_state_table[y][x][d_i] = Some(State { x: nxu, y: nyu, d });
                    }
                }
            }
        }
    }

    let mut visited_positions = std::collections::HashSet::new();
    let mut current = start_state;
    visited_positions.insert((current.x, current.y));

    loop {
        let d_i = dir_to_index(current.d);
        let ns = next_state_table[current.y][current.x][d_i];

        match ns {
            Some(new_state) => {
                visited_positions.insert((new_state.x, new_state.y));
                current = new_state;
            }
            None => {
                break;
            }
        }
    }

    let distinct_count = visited_positions.len();

    println!("Part1 : {}", distinct_count);
}
