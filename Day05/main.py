import re
input = [line.strip() for line in open("input.txt")]

def part1(input):
    currents = []
    nexts = [int(i) for i in re.findall('[0-9]+', input[0])]

    input = input[2:]
    input = [i for i in input if i != '']

    for line in input:
        numbers = re.findall('[0-9]+', line)
        if len(numbers) == 0:
            nexts.extend(currents)
            currents = nexts
            nexts = []
        else:
            numbers = [int(num) for num in numbers]
            current_destination = numbers[0]
            current_source = numbers[1]
            range_map = numbers[2]

            for cur_num in currents:
                if cur_num >= current_source and cur_num < current_source + range_map:
                    distance = cur_num - current_source 
                    nexts.append(current_destination + distance)
                    currents = [n for n in currents if n != cur_num]

    nexts.extend(currents)
    currents = nexts
    return min(currents)

def part2(input):
    currents = []
    nexts = [int(i) for i in re.findall('[0-9]+', input[0])]
    unmapped = []

    input = input[2:]
    input = [i for i in input if i != '']

    for line in input:
        numbers = re.findall('[0-9]+', line)
        if len(numbers) == 0:
            currents = nexts
            currents.extend(unmapped)
            nexts = []
            unmapped = []
        else:
            currents.extend(unmapped)
            unmapped = []
            numbers = [int(num) for num in numbers]
            current_destination = numbers[0]
            current_source = numbers[1]
            range_map = numbers[2]
            
            while len(currents) > 0:
                # if currents lower bound falls beneath the current source end and its upper bound 
                # falls above the current source start, that means that some or part of its range fits and must be mapped
                if currents[0] < current_source + range_map and currents[0] + currents[1] > current_source:
                    # start of part to be mapped
                    to_map_start = max(currents[0], current_source)
                    # range of part to be mapped
                    to_map_end = min(current_source + range_map, currents[0] + currents[1])
                    to_map_range = to_map_end - to_map_start

                    # to get mapped values, you take to_map_start - current_destination, which gives you the distance from the source start
                    # then you take the mapped range and add that to the source start to get the mapped end
                    # then you subtract the end from the start to get the range
                    mapped_start = current_destination + (to_map_start - current_source)
                    mapped_range = to_map_range
                    nexts.append(mapped_start)
                    nexts.append(mapped_range)
                    
                    # if the to be mapped start is the current destination and the current start and current destination are not the same
                    # there's some part of the current range that needs to be cut
                    if currents[0] < to_map_start:
                        left_start = currents[0]
                        left_end = current_source 
                        left_range = left_end - left_start
                        currents.append(left_start)
                        currents.append(left_range)

                    # same thing, but on the right
                    if currents[0] + currents[1] > to_map_end:
                        right_start = current_source + range_map
                        right_end = currents[0] + currents[1]
                        right_range = right_end - right_start
                        currents.append(right_start)
                        currents.append(right_range)
                else:
                    unmapped.append(currents[0])
                    unmapped.append(currents[1])

                currents.pop(0)
                currents.pop(0)


    currents = nexts
    currents.extend(unmapped)
    nexts = []
    unmapped = []

    actuals = [currents[i] for i in range(0, len(currents), 2)]
    return min(actuals);

print(part1(input))
print(part2(input))