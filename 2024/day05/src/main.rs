use std::collections::{HashMap, HashSet};
use utils;

fn parse_rules(rules: Vec<String>) -> HashMap<i32, HashSet<i32>> {
    let mut rule_map: HashMap<i32, HashSet<i32>> = HashMap::new();

    for rule in rules {
        let parts: Vec<&str> = rule.split('|').collect();
        if parts.len() == 2 {
            let page_a = parts[0].trim().parse::<i32>().unwrap();
            let page_b = parts[1].trim().parse::<i32>().unwrap();
            rule_map.entry(page_a).or_insert_with(HashSet::new).insert(page_b);
        }
    }

    rule_map
}

fn is_update_valid(update: Vec<i32>, rules: HashMap<i32, HashSet<i32>>) -> bool {
    let mut page_index_map = HashMap::new();

    for (index, &page) in update.iter().enumerate() {
        page_index_map.insert(page, index);
    }

    for (&page_a, dependents) in &rules {
        if let Some(&index_a) = page_index_map.get(&page_a) {
            for &page_b in dependents {
                if let Some(&index_b) = page_index_map.get(&page_b) {
                    if index_a >= index_b {
                        return false;
                    }
                }
            }
        }
    }

    true
}

fn topological_sort(update: &Vec<i32>, rule_map: &HashMap<i32, HashSet<i32>>) -> Vec<i32> {
    let set: HashSet<i32> = update.iter().cloned().collect();
    let mut in_degree = HashMap::new();

    for &page in update {
        in_degree.insert(page, 0);
    }

    for (&page_a, dependents) in rule_map {
        if set.contains(&page_a) {
            for &page_b in dependents {
                if set.contains(&page_b) {
                    *in_degree.get_mut(&page_b).unwrap() += 1;
                }
            }
        }
    }

    let mut queue = std::collections::VecDeque::new();
    for (&node, &deg) in &in_degree {
        if deg == 0 {
            queue.push_back(node);
        }
    }

    let mut result = Vec::new();
    while let Some(node) = queue.pop_front() {
        result.push(node);

        if let Some(dependents) = rule_map.get(&node) {
            for &dep in dependents {
                if let Some(d) = in_degree.get_mut(&dep) {
                    *d -= 1;
                    if *d == 0 {
                        queue.push_back(dep);
                    }
                }
            }
        }
    }

    result
}


fn main() {
    let input_rows: Vec<String> = utils::parse_lines("day05/src/input.txt");
    let mut rules: Vec<String> = Vec::new();
    let mut updates: Vec<Vec<i32>> = Vec::new();
    let mut is_update_section = false;

    for row in input_rows {
        if row.trim().is_empty() {
            is_update_section = true;
            continue;
        }

        if is_update_section {
            let update_row: Vec<i32> = row
                .split(',')
                .filter_map(|s| s.trim().parse::<i32>().ok())
                .collect();
            updates.push(update_row);
        } else {
            rules.push(row);
        }
    }
    let rule_map = parse_rules(rules);

    let mut total_corr_middle = 0;
    let mut total_incorr_sorted_middle = 0;
    for update in updates {
        let is_valid = is_update_valid(update.clone(), rule_map.clone());
        if is_valid {
            total_corr_middle += update[update.len()/2];
        }
        else {
            let sorted_update = topological_sort(&update.clone(), &rule_map);
            total_incorr_sorted_middle += sorted_update[update.len()/2];
        }
    }

    println!("Part1: {}", total_corr_middle);
    println!("Part2: {}", total_incorr_sorted_middle);
}