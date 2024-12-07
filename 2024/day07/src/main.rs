use utils;

fn parse_input(input: String) -> Vec<(u64, Vec<u64>)> {
    let mut output = Vec::new();
    for line in input.lines() {
        let (result, numbers) = line.split_once(": ").unwrap();
        output.push((
            result.parse().unwrap(),
            numbers.split(' ').map(|s| s.parse().unwrap()).collect(),
        ));
    }

    output
}

fn main() {
    let parsed_input = parse_input(utils::parse_to_string("day07/src/input.txt"));

    println!("Part1: {}", calculate_total(&parsed_input, 1));
    println!("Part2: {}", calculate_total(&parsed_input, 2));
}

fn calculate_total(parsed: &[(u64, Vec<u64>)], part: u32) -> u64 {
    let mut total = 0;
    for (result, numbers) in parsed {
        let combinations = if part == 2 {
            3_u32.pow(u32::try_from(numbers.len() - 1).unwrap())
        } else {
            2_u32.pow(u32::try_from(numbers.len() - 1).unwrap())
        };

        'outer: for i_original in 0..combinations {
            let mut i = i_original;
            let mut iter = numbers.iter();
            let mut test_result = *iter.next().unwrap();

            for n in iter {
                if part == 2 {
                    match i % 3 {
                        0 => test_result += n,
                        1 => test_result *= n,
                        2 => test_result = test_result * 10_u64.pow(n.ilog10() + 1) + n,
                        _ => unreachable!(),
                    }
                    i /= 3;
                } else {
                    if i & 1 == 0 {
                        test_result += n;
                    } else {
                        test_result *= n;
                    }
                    i >>= 1;
                }
            }

            if test_result == *result {
                total += result;
                break 'outer;
            }
        }
    }
    total
}
