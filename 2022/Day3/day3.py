def day_3_part_1(imput):
    SUM = 0
    for line in input.splitlines():
        SCORE = 0
        first, second = split_by_half(line)
        first_set, second_set = set(first), set(second)
        match = first_set & second_set
        if (match):
            matchStr = "".join(match)
            matchnum = ord(matchStr) - 96 if matchStr.islower() else (ord(matchStr) - 64) + 26
            SCORE += matchnum
        SUM += SCORE
    return SUM
        
def day_3_part_2(input):
    SUM = 0
    buffer = []
    inputs = input.splitlines()
    for idx, line in enumerate(inputs):
        buffer.append(line)
        SCORE = 0
        if ((idx + 1) % 3 == 0):
            a,b,c = buffer
            buffer = []
            SCORE += process_input(a,b,c)
        SUM += SCORE
    return SUM

def process_input(a, b, c):
    a_set, b_set, c_set = set(a), set(b), set(c)
    match = a_set & b_set & c_set
    if (match):
        matchStr = "".join(match)
        matchnum = ord(matchStr) - 96 if matchStr.islower() else (ord(matchStr) - 64) + 26
    return matchnum


def split_by_half(input):
    return input[:len(input)//2], input[len(input)//2:]

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input = f.read()
        print(day_3_part_1(input))
        print(day_3_part_2(input))