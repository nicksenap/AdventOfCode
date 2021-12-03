jigSum = lambda colums: sum([int(c) for c in colums]);

def main():
    inputfile = open('input.txt', 'r')
    rows = [[char for char in line] for line in inputfile]
    columns = list(zip(*rows))
    # Part 1
    gamma = epsilon = ''
    for i in range(len(columns)):
        result = jigSum(columns[i])
        if result > 500:
            epsilon += '0'
            gamma += '1'
        else:
            epsilon += '1'
            gamma += '0'
    a = int(epsilon,2) * int(gamma,2)
    print(a)
"""
    if result > 500:
"""
def getOxgen(rows, index = 0):
    if len(rows) == 1:
        return rows[0]
    rows = [row for row in rows if row[index] == '1']
    cols = list(zip(*rows))
    major = 1
    if jigSum(cols[index]) > len(cols[index]) / 2:
        major = 1
    else:
        major = 0
    rows = [row[0] == major for row in rows]
    getOxgen(rows, index + 1)


    


if __name__ == '__main__':
    main()