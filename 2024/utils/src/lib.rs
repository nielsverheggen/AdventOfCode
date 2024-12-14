use std::fs::File;
use std::{fs, io};
use std::io::BufRead;
use std::path::Path;
use std::str::FromStr;
use std::time::{Duration, Instant};

pub fn parse_to_string(path: &str) -> String {
    fs::read_to_string(path).expect("Should have been able to read the file")
}

pub fn parse_lines(path: &str) -> Vec<String> {
    parse_to_string(path)
        .lines()
        .map(String::from)
        .collect()
}

pub fn parse_lines_to<T: FromStr>(path: &str) -> Vec<T>
where
    T::Err: std::fmt::Debug,
{
    parse_to_string(path)
        .lines()
        .map(|line| line.parse::<T>().expect("Failed to parse line"))
        .collect()
}

pub fn parse_delimited<T: FromStr>(line: &str, delimiter: &str) -> Vec<T>
where
    T::Err: std::fmt::Debug,
{
    line.split(delimiter)
        .map(|item| item.parse::<T>().expect("Failed to parse item"))
        .collect()
}

pub fn find_max<T: Ord>(items: &[T]) -> Option<&T> {
    items.iter().max()
}

pub fn find_min<T: Ord>(items: &[T]) -> Option<&T> {
    items.iter().min()
}

pub fn sum_of<T: std::iter::Sum + std::clone::Clone>(items: &[T]) -> T {
    items.iter().cloned().sum()
}

pub fn product_of<T: std::iter::Product + std::clone::Clone>(items: &[T]) -> T {
    items.iter().cloned().product()
}

pub fn generate_permutations<T: Clone>(items: &[T]) -> Vec<Vec<T>> {
    let mut permutations = Vec::new();
    permute(items.to_vec(), vec![], &mut permutations);
    permutations
}

fn permute<T: Clone>(remaining: Vec<T>, current: Vec<T>, result: &mut Vec<Vec<T>>) {
    if remaining.is_empty() {
        result.push(current);
        return;
    }
    for i in 0..remaining.len() {
        let mut new_remaining = remaining.clone();
        let mut new_current = current.clone();
        new_current.push(new_remaining.remove(i));
        permute(new_remaining, new_current, result);
    }
}

pub fn parse_grid_delim<T: FromStr>(input: &str, row_delim: &str, col_delim: &str) -> Vec<Vec<T>>
where
    T::Err: std::fmt::Debug,
{
    input
        .split(row_delim)
        .map(|row| parse_delimited(row, col_delim))
        .collect()
}

pub fn parse_grid(directory: &str) -> Vec<Vec<char>> {
    let filepath = Path::new(directory);
    let file = File::open(filepath).expect("File not found");
    let reader = io::BufReader::new(file);
    let grid: Vec<Vec<char>> = reader
        .lines()
        .filter_map(|line| line.ok()) 
        .map(|line| line.trim().chars().collect())
        .collect();
    
    grid
}

pub fn bfs(start: usize, graph: &[Vec<usize>]) -> Vec<usize> {
    let mut visited = vec![false; graph.len()];
    let mut queue = vec![start];
    let mut result = Vec::new();

    while let Some(node) = queue.pop() {
        if visited[node] {
            continue;
        }
        visited[node] = true;
        result.push(node);

        for &neighbor in &graph[node] {
            if !visited[neighbor] {
                queue.insert(0, neighbor);
            }
        }
    }

    result
}

pub fn dfs(start: usize, graph: &[Vec<usize>]) -> Vec<usize> {
    let mut visited = vec![false; graph.len()];
    let mut stack = vec![start];
    let mut result = Vec::new();

    while let Some(node) = stack.pop() {
        if visited[node] {
            continue;
        }
        visited[node] = true;
        result.push(node);

        for &neighbor in &graph[node] {
            if !visited[neighbor] {
                stack.push(neighbor);
            }
        }
    }

    result
}

pub fn gcd(a: isize, b: isize) -> isize {
    if b == 0 {
        a.abs()
    } else {
        gcd(b, a % b)
    }
}

pub fn start_execution_timing() -> Instant {
    Instant::now()
}

pub fn end_execution_timing(execution_time_start: Instant) -> Duration {
    execution_time_start.elapsed()
}