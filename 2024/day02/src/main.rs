use utils;

fn is_safe_report(levels: Vec<i32>) -> bool {
    if levels.len() < 2 {
        return true;
    }

    let mut direction = 0;

    for i in 1..levels.len() {
        let diff = levels[i] - levels[i - 1];

        if diff.abs() < 1 || diff.abs() > 3 {
            return false;
        }

        let current_direction = if diff > 0 { 1 } else { -1 };

        if direction == 0 {
            direction = current_direction;
        } else if direction != current_direction {
            return false;
        }
    }

    true
}

fn main() {
    let input_rows = utils::parse_lines("day02/src/input.txt");
    let mut reports: Vec<Vec<i32>> = Vec::new();

    for line in input_rows {
        let mut report: Vec<i32> = Vec::new();
        let parts: Vec<&str> = line.split_whitespace().collect();

        for part in parts {
            let level: i32 = part.parse().expect("Failed to parse to i32");
            report.push(level);
        }
        reports.push(report);
    }
    let mut safe_reports: i32 = 0;
    for report in &reports {
        if is_safe_report(report.clone()) == true {
            safe_reports += 1;
        }
    }

    println!("Part1: {}", safe_reports);

    let mut safe_reports_ext: i32 = 0;
    for report in &reports {
        if is_safe_report(report.clone()) == true {
            safe_reports_ext += 1;
        } else {
            for i in 0..report.clone().len() {
                let mut red_report = report.clone();
                red_report.remove(i);
                if is_safe_report(red_report) == true {
                    safe_reports_ext += 1;
                    break;
                }
            }
        }
    }
    println!("Part2: {}", safe_reports_ext);
}