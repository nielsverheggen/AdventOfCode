import re

input = [line.strip() for line in open("input.txt")]

def part1(input):
    totalCalValue= 0
    for line in input:
        lineOfNumbers = ""
    
        for character in line:
            if re.match('^[0-9]+$', character):
                lineOfNumbers += character

        totalCalValue += int(lineOfNumbers[0] + lineOfNumbers[len(lineOfNumbers) - 1])
    return totalCalValue

str2num = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

def part2(input):
    totalCalValue= 0
    for line in input:
        line = replace_words(line)
        lineOfNumbers = ""
    
        for character in line:
            if re.match('^[0-9]+$', character):
                lineOfNumbers += character

        totalCalValue += int(lineOfNumbers[0] + lineOfNumbers[len(lineOfNumbers) - 1])
    return totalCalValue

def replace_words(text):
    for k, v in str2num.items():
        text = text.replace(k, v)
    return text


# print(part1(input))
print(part2(input))