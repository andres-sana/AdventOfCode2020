inp = open('InputData.txt').read().split('\n')

def findCombination():
    for x in range(len(inp)):
        firstEntry = int(inp[x])
        for i in range(len(inp)):
            secondEntry = int(inp[i])
            if firstEntry + secondEntry == 2020:
                return firstEntry * secondEntry  

print(findCombination())
