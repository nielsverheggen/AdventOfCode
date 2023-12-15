import re

def parse_input():
    with open("input.txt", 'r') as file:
        content = file.read()
        steps = content.split(',')
        return steps

def get_hash(step):
    curval = 0 
    for char in step:
        curval = (curval + ord(char)) * 17 % 256
        
    return curval

def part1(input):
    totalValue = 0
    for step in input:
        totalValue += get_hash(step)
    
    return totalValue

print(part1(parse_input()))

def part2(input):
    boxes = {}
    for step in input:
        label = re.match(r"^[^-=]*", step).group(0)
        boxnr = get_hash(label)
        if '='  in step:
            focal_length = step.split("=",1)[1]
            if boxnr not in boxes:
                boxes[boxnr] = {}
                boxes[boxnr][label] = focal_length
            else:
                if label in boxes[boxnr]:
                    boxes[boxnr][label] = focal_length
                else:
                    boxes[boxnr][label] = focal_length
                
        else:
            if boxnr in boxes and label in boxes[boxnr]:
                boxes[boxnr].pop(label)
                if len(boxes[boxnr]) == 0:
                    boxes.pop(boxnr)
    
    total_focus_power = 0
    for box in boxes:
        for lens in boxes[box]:
            a = int(box + 1)
            b = int(list(boxes[box].keys()).index(lens) + 1)
            c = int(boxes[box][lens])
            total_focus_power += (a * b * c)
        
    return total_focus_power
        
    
print(part2(parse_input()))