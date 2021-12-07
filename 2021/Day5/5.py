from collections import Counter
import re

def part1(lines):
    points = Counter()
    for line in lines:
        value = [int(find) for find in re.findall('[0-9]+', line)] 
        x0, y0 = value[0], value[1]
        x1, y1 = value[2], value[3]
        if x0 == x1:
            points.update((x0, y) for y in range(min(y0, y1), max(y0, y1) + 1))
        elif y0 == y1:
            points.update((x, y0) for x in range(min(x0, x1), max(x0, x1) + 1))
    return sum(count > 1 for count in points.values())


def part2(lines):
    points = Counter()
    for line in lines:
        value = [int(find) for find in re.findall('[0-9]+', line)] 
        x0, y0 = value[0], value[1]
        x1, y1 = value[2], value[3]
        if x0 == x1:
            points.update((x0, y) for y in range(min(y0, y1), max(y0, y1) + 1))
        elif y0 == y1:
            points.update((x, y0) for x in range(min(x0, x1), max(x0, x1) + 1))
        elif abs(x1 - x0) == abs(y1 - y0):
            dx = 1 if x1 > x0 else -1
            dy = 1 if y1 > y0 else -1
            points.update((x0 + i * dx, y0 + i * dy) for i in range(abs(x1 - x0) + 1))
    return sum(count > 1 for count in points.values())

def main():
    inputfile = open('input.txt', 'r')
    lines = inputfile.readlines()
    print(part2(lines))

if __name__ == "__main__":
    main()