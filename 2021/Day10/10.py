pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
part1_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
part2_points = {")": 1, "]": 2, "}": 3, ">": 4}


def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        print('part1: ', part1(lines))
        print('part2: ', part2(lines))


def part1(lines):
    total = 0
    for line in lines:
        expected = []
        for char in line.strip():
            if char in pairs:
                expected.append(pairs[char])
            elif not expected or char != expected.pop():
                total += part1_points[char]
                break
    return total


def part2(lines):
    scores = []
    for line in lines:
        expected = []
        for char in line.strip():
            if char in pairs:
                expected.append(pairs[char])
            elif not expected or char != expected.pop():
                break
        else:
            score = 0
            for char in expected[::-1]:
                score = 5 * score + part2_points[char]
            scores.append(score)
    scores.sort()
    return scores[len(scores) // 2]


if __name__ == "__main__":
    main()
