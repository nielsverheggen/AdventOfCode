use utils;

fn main() {
    let input_rows = utils::parse_lines("day01/src/input.txt");
    let mut col1: Vec<i32> = Vec::new();
    let mut col2: Vec<i32> = Vec::new();

    for line in input_rows {
        let parts: Vec<&str> = line.split_whitespace().collect();
        if parts.len() == 2 {
            let num1: i32 = parts[0]
                .parse()
                .expect("Failed to parse number in column 1");
            let num2: i32 = parts[1]
                .parse()
                .expect("Failed to parse number in column 2");

            col1.push(num1);
            col2.push(num2);
        } else {
            panic!("Each row must contain exactly two parts");
        }
    }
    col1.sort();
    col2.sort();

    let total_distance: i32 = col1
        .iter()
        .zip(col2.iter()) 
        .map(|(a, b)| (a - b).abs())
        .sum();

    println!("Part1: {}", total_distance);

    let mut similarity = 0;
    for &score in &col1 {
        similarity += score * col2.iter().filter(|&&x| x == score).count() as i32;
    }

    println!("Part2: {}", similarity);
}