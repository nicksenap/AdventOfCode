def day_4_part_1(input):
    SUM = 0
    for line in input.splitlines():
        SCORE = 0
        a1, a2, b1, b2 = better_spilt(line)
        if containes_range(a1, a2, b1, b2):
            SUM += 1
        SUM += SCORE
    return SUM

def day_4_part_2(input):
    SUM = 0
    for line in input.splitlines():
        SCORE = 0
        a1, a2, b1, b2 = better_spilt(line)
        if set(range(a1, a2+1)) & set(range(b1, b2+1)):
            SUM += 1
        SUM += SCORE
    return SUM

def better_spilt(input):
    a, b = input.strip().split(',')
    a1, a2 = map(int, a.split('-'))
    b1, b2 = map(int, b.split('-')) 
    return a1, a2, b1, b2

def containes_range(a1, a2, b1, b2):
    return a1 <= b1 and a2 >= b2 or b1 <= a1 and b2 >= a2


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input = f.read()
        print(day_4_part_1(input))
        print(day_4_part_2(input))