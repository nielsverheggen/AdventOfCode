use utils;
use regex::Regex;

fn main() {
    let input = utils::parse_to_string("day03/src/input.txt");
    let matches: Vec<&str> = Regex::new(r"mul\(\d{1,3},\d{1,3}\)").unwrap()
        .find_iter(&input)
        .map(|mat| mat.as_str())
        .collect();

    let mut total: i32 = 0;
    for mul_match in matches {
        let numbers: Vec<&str> = Regex::new(r"(\d{1,3})").unwrap()
            .find_iter(&mul_match)
            .map(|mat| mat.as_str())
            .collect();

        let one: i32 = numbers[0].parse().expect("Failed to parse to i32");
        let two: i32 = numbers[1].parse().expect("Failed to parse to i32");

        total += one * two;
    }

    println!("Part1: {}", total);

    let acc_matches: Vec<&str> = Regex::new(r"(?:mul\(\d{1,3},\d{1,3}\)|(do)\(\)|(don)'t\(\))").unwrap()
        .find_iter(&input)
        .map(|mat| mat.as_str())
        .collect();

    let mut total_if_enabled: i32 = 0;
    let mut enabled = true;

    for cur_match in acc_matches {
        if cur_match == "do()" {
            enabled = true;
        } else if cur_match == "don't()" {
            enabled = false;
        } else {
            if !enabled {
                continue;
            }
            let numbers: Vec<&str> = Regex::new(r"(\d{1,3})").unwrap()
                .find_iter(&cur_match)
                .map(|mat| mat.as_str())
                .collect();

            let one: i32 = numbers[0].parse().expect("Failed to parse to i32");
            let two: i32 = numbers[1].parse().expect("Failed to parse to i32");

            total_if_enabled += one * two;
        }
    }

    println!("Part2: {}", total_if_enabled)
}
