import re

def main():
    inputfile = open('input.txt', 'r')
    lines = [i.replace('\n', '') for i in inputfile.readlines()]
    # Part 1
    # horizontal = depth = 0
    # for line in lines:
    #     operator = re.search('[a-z]+', line).group()
    #     value = int(re.search('[0-9]+', line).group())
    #     if operator == 'forward': horizontal += value
    #     if operator == 'down': depth += value
    #     if operator == 'up': depth -= value 
    # print('horizontal', horizontal, 'depth', depth)
    # return horizontal * depth

    # Part 2
    horizontal = depth = aim = 0
    for line in lines:
        operator = re.search('[a-z]+', line).group()
        value = int(re.search('[0-9]+', line).group())
        if operator == 'forward': 
            horizontal += value
            depth += value * aim
        if operator == 'down': aim += value
        if operator == 'up': aim -= value 
    print('horizontal', horizontal, 'depth', depth, 'aim', aim)
    return horizontal * depth
    
if __name__ == "__main__":
    print(main())