from copy import deepcopy

def parse_input(file_path):
    with open(file_path) as file:
        sections = file.read().split("\n\n")

    rules_data = sections[0].split("\n")
    rules = {key: values[:-1].split(",") for key, values in (line.split("{") for line in rules_data)}

    items = sections[1].split("\n")

    return rules, items

rules, items = parse_input("input.txt")

def main1(item, rules):
    curr_rule = "in"
    while True:
        for i in rules[curr_rule]:
            if ":" in i: 
                cond, act = i.split(":")
                key, value = cond.split(">") if ">" in cond else cond.split("<")
                value = int(value)

                condition_met = (item[key] > value if ">" in cond else item[key] < value)
                if condition_met:
                    if act in ["A", "R"]:
                        return act == "A"
                    curr_rule = act
                    break
            else:
                if i in ["A", "R"]:
                    return i == "A"
                curr_rule = i

def part1(items, rules):
    total = 0
    for i in items:
        item = {k: int(v) for k, v in (pair.split("=") for pair in i[1:-1].split(","))}
        if main1(item, rules):
            total += sum(item.values())
    return total

print(part1(items, rules))

rules, items = parse_input("input.txt")

def calculate_size(range_dict):
    total_product = 1
    for lower, upper in range_dict.values():
        total_product *= upper - lower + 1
    return total_product

def main2(range, flow):
    result = 0
    for rule in rules[flow]:
        if ":" in rule:
            condition, action = rule.split(":")
            new_range = deepcopy(range)
            a, b = extract_condition(condition)
            is_condition_met = check_condition(new_range, a, b, condition)

            if is_condition_met:
                update_rng(new_range, range, a, b, condition)
                result += perform_action(new_range, action)

        else:
            result += handle_simple_rule(range, rule)
    return result

def extract_condition(condition):
    if ">" in condition:
        return condition.split(">")
    elif "<" in condition:
        return condition.split("<")

def check_condition(range, a, b, condition):
    if ">" in condition and range[a][1] > int(b):
        return True
    elif "<" in condition and range[a][0] < int(b):
        return True
    return False

def update_rng(new_range, range, a, b, condition):
    if ">" in condition:
        new_range[a][0] = max(new_range[a][0], int(b) + 1)
        range[a][1] = min(range[a][1], int(b))
    elif "<" in condition:
        new_range[a][1] = min(new_range[a][1], int(b) - 1)
        range[a][0] = max(range[a][0], int(b))

def perform_action(range, action):
    if action == "A":
        return calculate_size(range)
    elif action != "R":
        return main2(range, action)
    return 0

def handle_simple_rule(range, rule):
    if rule == "A":
        return calculate_size(range)
    elif rule != "R":
        return main2(range, rule)
    return 0

print(main2({"x":[1,4000], "m":[1,4000], "a":[1,4000], "s":[1,4000]}, "in"))