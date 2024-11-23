from functools import cache

def parse_input():
    return [line.strip().split() for line in open("input.txt").readlines()]

@cache
def count_valid_arrangements(springs, groups):

    springs = springs.lstrip('.')

    if springs == '':
        return int(groups == ()) 

    if groups == ():
        return int(springs.find('#') == -1) 

    # starts with '#' so remove the first spring
    if springs[0] == '#':
        if len(springs) < groups[0] or '.' in springs[:groups[0]]:
            return 0 # impossible - not enough space for the spring
        elif len(springs) == groups[0]:
            return int(len(groups) == 1) # single spring with right size
        elif springs[groups[0]] == '#':
            return 0 # springs must be separated by '.' (or '?') 
        else:
            return count_valid_arrangements(springs[groups[0]+1:], groups[1:]) # recursion with one less spring

    # count_valid_arrangements if converted the first '?' to '#' + '.'
    return count_valid_arrangements('#'+springs[1:],groups) + count_valid_arrangements(springs[1:],groups)


input = parse_input()

data1 = []
for data in input:
    springs = data[0]
    groups = tuple(int(size) for size in data[1].split(','))
    data1.append([springs, groups])

print(sum(count_valid_arrangements(springs, groups) for [springs, groups] in data1))

data2 = []
for spring in data1:
    springs = (spring[0] + '?') * 4 + spring[0]
    damaged_groups = spring[1] * 5
    data2.append([springs, damaged_groups])
    
print(sum(count_valid_arrangements(springs, groups) for [springs, groups] in data2))
