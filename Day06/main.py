def read_file1(filename):

    with open(filename, 'r') as file:
        lines = file.readlines()

    time_values = list(map(int, lines[0].split()[1:]))
    distance_values = list(map(int, lines[1].split()[1:]))

    time_distance = dict(zip(time_values, distance_values))

    return time_distance

def read_file2(filename):

    with open(filename, 'r') as file:
        lines = file.readlines()

    time_values = list(map(int, lines[0].split()[1:]))
    distance_values = list(map(int, lines[1].split()[1:]))
    time = ""
    for x in time_values:
        time += str(x)

    distance = ""
    for x in distance_values:
        distance += str(x) 
    
    time_distance = {int(time): int(distance)}

    return time_distance


def main(input):
    allNrOfWaysToBeat = 1
    for time, distance in input.items():
        nrOfWaysToBeat = 0
        for holdTime in range(time + 1):
            timeLeft = time - holdTime
            traveled = holdTime * timeLeft
            if traveled > distance:
                nrOfWaysToBeat += 1
    
        allNrOfWaysToBeat *= nrOfWaysToBeat
        
    return allNrOfWaysToBeat
    
# print(main(read_file1('input')))
print(main(read_file2('input')))

