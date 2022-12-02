
DICT_SCORE = {"A": 1, "B": 2, "C": 3}
RESULT_SCORE = {"X": 0, "Y": 3, "Z": 6}
DICT_WINNER = {"A": "B", "B": "C", "C": "A"}
DICT_LOSER = {"A": "C", "B": "A", "C": "B"}
DICT_DRAW = {"A": "A", "B": "B", "C": "C"}
DICT_TO_USE = {"X": DICT_LOSER, "Y": DICT_DRAW, "Z": DICT_WINNER}
DICT = {"X": "A", "Y": "B", "Z": "C"}



def day_2_part_1(input):
    SUM = 0
    for line in input.splitlines():
        SCORE = 0
        opponent, you = line.split(" ")
        you = DICT[you]
        SCORE += DICT_SCORE[you]
        if you == opponent:
            SCORE += 3
        elif you == DICT_WINNER[opponent]:
            SCORE += 6   
        SUM += SCORE
    return SUM

def day_2_part_2(input):
    SUM = 0
    for line in input.splitlines():
        SCORE = 0
        opponent, resulat = line.split(" ")
        dict_to_use = DICT_TO_USE[resulat]
        you = dict_to_use[opponent]
        SCORE += DICT_SCORE[you]
        SCORE += RESULT_SCORE[resulat]
        SUM += SCORE
    return SUM

        
if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input = f.read()
        print(day_2_part_1(input))
        print(day_2_part_2(input))