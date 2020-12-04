inp = open('InputData.txt').read().split('\n')

x = 0
amt = 0

for i in range(len(inp)):
    if i < len(inp)-1:
        i = i+1
    else:
        break
    line = str(inp[i])
    x = x + 3
    if x >= len(line) - 1:
        x = x - (len(line))
    site = line[x]
    if site == '#':
        amt = amt + 1

print(amt)
