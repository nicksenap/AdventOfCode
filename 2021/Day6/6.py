def main():
    with open("input.txt", "r") as f:
        line = f.read()
        lineList = [int(item) for item in line.split(',')]
        for i in range(256):
            print(i)
            # print(lineList)
            lineList = agg(lineList)
        print(len(lineList))

def forward(day):
    return 6 if day == 0 else day - 1

def agg(lineList):
    return list(map(forward, lineList))  + [8] * lineList.count(0) 

if __name__ == "__main__":
    main()