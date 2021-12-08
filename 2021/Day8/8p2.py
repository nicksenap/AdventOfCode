def decode_dictionary(inp):
    digits = {}
    five_len, six_len = [], []

    for digit in inp:
        if len(digit) == 2:
            digits["1"] = set(digit)
        elif len(digit) == 4:
            digits["4"] = set(digit)
        elif len(digit) == 3:
            digits["7"] = set(digit)
        elif len(digit) == 7:
            digits["8"] = set(digit)
        elif len(digit) == 5:
            five_len.append(set(digit))
        elif len(digit) == 6:
            six_len.append(set(digit))

    for digit in five_len:
        # 2, 3, 5
        if len(digit & digits["1"]) and len(digit & digits["4"]) == 2:
            digits["2"] = digit
        elif len(digit & digits["7"]) == 3:
            digits["3"] = digit
        elif len(digit & digits["1"]) == 1 and len(digit & digits["4"]) == 3:
            digits["5"] = digit

    for digit in six_len:
        # 6, 9, 0
        if len(digit & digits["1"]) == 1:
            digits["6"] = digit
        elif len(digit & digits["4"]) == 4:
            digits["9"] = digit
        elif len(digit & digits["4"]) == 3:
            digits["0"] = digit

    decoded = {"".join(sorted(v)): k for k, v in digits.items()}
    return decoded


def part2(problem):
    sum = 0
    for inp, out in problem:
        decoded = decode_dictionary(inp)
        result = []
        for digit in out:
            digit = "".join(sorted(digit))
            result.append(decoded[digit])
        sum += int("".join(result))
    return sum


if __name__ == "__main__":
    problem = []
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            inp, out = line.split(" | ")
            inp, out = inp.split(), out.split()
            problem.append((inp, out))

    print(part2(problem))
