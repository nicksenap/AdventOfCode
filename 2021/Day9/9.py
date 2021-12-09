from math import prod


def main():
    with open('input.txt') as f:
        data = f.readlines()
        print("Part 1:", part1(data))
        print("Part 2:", part2(data))


def is_low_point(data, index):
    x, y = index
    lst = find_pts_around(data, index)
    for point in lst:
        if data[x][y] >= point:
            return False
    return True


def find_pts_around(data, index):
    x, y = index
    if x == 0:
        if y == 0:
            return [data[x+1][y], data[x][y+1]]
        elif y == len(data[0]) - 1:
            return [data[x+1][y], data[x][y-1]]
        else:
            return [data[x+1][y], data[x][y-1], data[x][y+1]]
    if y == 0:
        if x == len(data) - 1:
            return [data[x-1][y], data[x][y+1]]
        else:
            return [data[x-1][y], data[x+1][y], data[x][y+1]]
    if x == len(data) - 1:
        if y == len(data[0]) - 1:
            return [data[x-1][y], data[x][y-1]]
        return [data[x-1][y], data[x][y-1], data[x][y+1]]
    if y == len(data[0]) - 1:
        return [data[x-1][y], data[x+1][y], data[x][y-1]]
    return [data[x-1][y], data[x+1][y], data[x][y-1], data[x][y+1]]


def part1(lines):
    data = [[int(d) for d in da.strip()] for da in lines]
    result = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if is_low_point(data, (i, j)):
                result += data[i][j] + 1
    return result


def part2(lines):
    basins = []
    visited = [[False for _ in line.strip()] for line in lines]
    for i, line in enumerate(lines):
        for j, c in enumerate(line.strip()):
            if visited[i][j] or not ("0" <= c < "9"):
                continue
            basin = {(i, j)}
            stack = [(i, j)]
            while stack:
                i2, j2 = stack.pop()
                visited[i2][j2] = True
                for i3, j3 in ((i2 - 1, j2), (i2, j2 - 1), (i2, j2 + 1), (i2 + 1, j2)):
                    if (
                        0 <= i3 < len(lines)
                        and 0 <= j3 < len(lines[i3].strip())
                        and "0" <= lines[i3][j3] < "9"
                        and (i3, j3) not in basin
                    ):
                        basin.add((i3, j3))
                        stack.append((i3, j3))
            basins.append(len(basin))
    return prod(sorted(basins)[-3:])


if __name__ == '__main__':
    main()
