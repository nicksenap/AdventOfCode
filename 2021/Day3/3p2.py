from collections import Counter

def main():
    inputfile = open('input.txt', 'r')
    lines = inputfile.readlines()
    o2 = lines
    co2 = lines
    i = 0
    while len(o2) > 1 or len(co2) > 1:
        major = max(Counter(s[i] for s in o2).items(), key=lambda entry: (entry[1], entry[0]))[0]
        minor = min(Counter(s[i] for s in co2).items(), key=lambda entry: (entry[1], entry[0]))[0]
        o2 = [s for s in o2 if s[i] == major]
        co2 = [s for s in co2 if s[i] == minor]
        i += 1
    print(int(o2[0], 2) * int(co2[0], 2))


if __name__ == '__main__':
    main()