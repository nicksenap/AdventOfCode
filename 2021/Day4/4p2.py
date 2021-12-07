import itertools

def parse(lines):
    it = iter(lines)
    draws = [int(draw) for draw in next(it).split(",")]
    boards = [
        [[int(item) for item in line.split()] for line in group]
        for key, group in itertools.groupby(it, key=lambda line: bool(line.strip()))
        if key
    ]
    return draws, boards


def mark(board, draw):
    for row in board:
        for i in range(len(row)):
            if row[i] == draw:
                row[i] = None


def isbingo(board):
    if any(all(item is None for item in row) for row in board):
        return True
    try:
        column = 0
        while True:
            if all(row[column] is None for row in board):
                return True
            column += 1
    except IndexError:
        return False

def part2(lines):
    draws, boards = parse(lines)
    for i, draw in enumerate(draws):
        for board in boards:
            mark(board, draw)
            if isbingo(board):
                score = draw * sum(filter(None, itertools.chain.from_iterable(board)))
        boards = [board for board in boards if not isbingo(board)]
        if not boards:
            break
    return score

def main():
    with open("input.txt") as f:
        lines = f.readlines()
    print(part2(lines))

if __name__ == "__main__":
    main()
