def main():
    with open("example.txt", "r") as f:
        line = f.read()
        # print(part1(line))
        print(part2(line))

def median(lst):
    lst.sort()
    if len(lst) % 2 == 0:
        return (lst[len(lst) // 2] + lst[(len(lst) - 1) // 2]) / 2
    else:
        return lst[len(lst) // 2]

def part1(line):
    lineList = [int(item) for item in line.split(',')]
    median_value = int(median(lineList))
    return sum([abs(foo - median_value) for foo in lineList])

def part2(line):
    lineList = [int(item) for item in line.split(',')]
    print(distance(lineList, lineList[0]))
    # used = set()
    # unique = [x for x in lineList if x not in used and (used.add(x) or True)]
    # print(len(unique))

def distance(list, value):
    return [sum(range(abs(foo - value) + 1)) for foo in list]

if __name__ == "__main__":
    main()