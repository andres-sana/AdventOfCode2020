inp = open('input01.txt').read().split('\n')

for x in range(len(inp)):
    firstEntry = int(inp[x])
    for i in range(len(inp)):
        secondEntry = int(inp[i])
        for k in range(len(inp)):
            thirdEntry = int(inp[k])
            if firstEntry + secondEntry + thirdEntry == 2020:
                print(firstEntry * secondEntry * thirdEntry)
            
