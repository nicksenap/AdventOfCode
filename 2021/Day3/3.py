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


if __name__ == '__main__':
    main()