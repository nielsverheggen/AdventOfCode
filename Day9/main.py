def parse_input(file_path='input.txt'):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        result = [list(map(int, line.split())) for line in lines]
    return result

def contains_only_zeros(array):
    return all(x == 0 for x in array)

def getHistory(history):
    prevStep = None
    differences = []
    for step in history:
        if prevStep is not None:
            if prevStep < step:
                differences.append(abs(step - prevStep))
            else: 
                differences.append((prevStep - step) * -1)

        prevStep = step
    return differences

def main(input):
    sxplv = 0
    for history in input:
        nextHistories = [history]
        if len(nextHistories) == 1:
            nextHistories.append(getHistory(history))
        
        while not contains_only_zeros(nextHistories[len(nextHistories) - 1]):
            nextHistories.append(getHistory(nextHistories[len(nextHistories) - 1]))
        
        index = 0
        nextValue = 0
        for rHistory in reversed(nextHistories):
            nextValue = rHistory[len(rHistory) -1] + nextValue
            if index == len(nextHistories) - 1:
                sxplv += nextValue
            
            index += 1
        
    return sxplv
        
print(main(parse_input()))
input = parse_input()
for history in input:
    history.reverse()
print(main(input))