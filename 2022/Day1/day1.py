

def day_1_part_1(input: str):
    SUM=0
    MAX=0
    for line in input.splitlines()[1:]:
        if line.isnumeric():
            SUM += int(line)
        else:
            MAX = max(MAX, SUM)
            SUM = 0
    return MAX

def day_1_part_2(input : str):
    SUM=0
    MAX_ARRAY=[]
    for line in input.splitlines()[1:]:
        if line.isnumeric():
            SUM += int(line)
        else:
            MAX_ARRAY.append(SUM)
            SUM = 0
    MAX_ARRAY.sort(reverse=True)
    return sum(MAX_ARRAY[:3])

        
if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input = f.read()
        print("Day 1: part 1: " + str(day_1_part_1(input)))
        print("Day 1: part 2: " + str(day_1_part_2(input)))