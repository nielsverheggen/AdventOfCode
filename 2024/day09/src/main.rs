use utils;

fn calc_checksum(list: Vec<i64>) -> i64 {
    list.iter()
        .enumerate()
        .map(|(i, &num)| (i as i64) * num)
        .sum()
}

fn main() {
    let execution_time_start = utils::start_execution_timing();

    let rawinput = utils::parse_to_string("day09/src/input.txt");

    let lengths: Vec<usize> = rawinput.trim().chars()
        .map(|c| c.to_digit(10).expect("Invalid digit") as usize)
        .collect();

    let mut list: Vec<i64> = lengths.iter()
        .enumerate()
        .flat_map(|(i, &num)| (0..num).map(move |_| if i % 2 == 0 { (i / 2) as i64 } else { -1 }))
        .collect();

    while list.contains(&-1) {
        if let Some(last) = list.last() {
            if *last == -1 {
                list.pop();
            } else {
                if let Some(index) = list.iter().position(|&x| x == -1) {
                    list[index] = list.pop().unwrap();
                }
            }
        }
    }

    println!("Part1: {}", calc_checksum(list));

    let chars: Vec<char> = rawinput.chars().collect();
    let mut d: Vec<(i32, i32)> = chars.iter().enumerate().map(|(idx, &ch)| {
        let i = idx + 1;
        let i_data = if i % 2 != 0 { (i as i32 / 2) + 1 } else { 0 };
        let i_size = ch.to_digit(10).unwrap_or(0) as i32;
        (i_data, i_size)
    }).collect();

    for i in (0..d.len()).rev() {
        for j in 0..i {
            if i >= d.len() || j >= d.len() {
                break;
            }

            let (i_data, i_size) = d[i];
            let (j_data, j_size) = d[j];

            if i_data != 0 && j_data == 0 && i_size <= j_size {
                d[i] = (0, i_size);
                d[j] = (0, j_size - i_size);
                d.insert(j, (i_data, i_size));
            }
        }
    }

    let mut flattened: Vec<i32> = Vec::new();
    for (d, s) in &d {
        for _ in 0..*s {
            flattened.push(*d);
        }
    }

    let mut sum_result: i64 = 0i64;
    for (i, c) in flattened.iter().enumerate() {
        if *c != 0 {
            sum_result += (i as i64) * ((c - 1) as i64);
        }
    }
    
    println!("Part2: {}", sum_result);

    println!("Elapsed: {:?}", utils::end_execution_timing(execution_time_start))
}
