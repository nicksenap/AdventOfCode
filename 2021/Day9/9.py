def main():
    with open('input.txt') as f:
        data = f.readlines()
        data = [[int(d) for d in da.strip()] for da in data]
        result = 0
        for i in range(len(data)):
            for j in range(len(data[0])):
                if is_low_point(data, (i, j)):
                    result += data[i][j] + 1
        print(result)


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


if __name__ == '__main__':
    main()
