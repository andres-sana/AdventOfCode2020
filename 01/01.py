inp = open('input01.txt').read().split('\n')

for x in range(len(inp)):
    firstEntry = int(inp[x])
    for i in range(len(inp)):
        secondEntry = int(inp[i])
        if firstEntry + secondEntry == 2020:
            print(firstEntry * secondEntry)
