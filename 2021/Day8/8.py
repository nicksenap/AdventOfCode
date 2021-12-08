def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        print(part1(lines))
       
        

    zero = ['a', 'b', 'c', 'f', 'g'] # 5
    one = ['c', 'f'] # 2
    two = ['a', 'c', 'd', 'e', 'g'] # 5
    three = ['a', 'c', 'd', 'f', 'g'] # 5
    four = ['b','c','d', 'f'] # 4
    five = ['a','b','d','f','g'] # 5
    six = ['a','b','d','e','f','g'] # 6
    seven = ['a','c','f'] # 3
    eight = ['a','b','c','d','e','f','g'] # 7
    nine = ['a','b','c','d','f','g'] # 6

def part1(lines):
    result = []
    for line in lines:
        _ , output = line.split(' | ')
        result.append(len([o for o in output.strip().split(' ') if len(o) in [2, 4, 3, 7]]))
    return sum(result)

# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
if __name__ == '__main__':
    main()