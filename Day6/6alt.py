def solve(times, lines):
    fishes = [0] * 9
    for line in lines:
        for fish in line.strip().split(","):
            fishes[int(fish)] += 1
    for _ in range(times):
        zero = fishes[0]
        fishes[0:8] = fishes[1:]
        fishes[6] += zero
        fishes[8] = zero
    return sum(fishes)


def part1(lines):
    return solve(80, lines)


def part2(lines):
    return solve(256, lines)


if __name__ == "__main__":
    print(part2(open("input.txt").readlines()))