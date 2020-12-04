inp = open('InputData.txt').read().split('\n')

def calculate(xM, yM):
    x = 0
    amt = 0
    for k in range(yM, len(inp), yM):
        if k >= len(inp):
            break
        line = str(inp[k])
        x = x + xM
        if x >= len(line) - 1:
            x = x - (len(line))
        site = line[x]
        if site == '#':
            amt = amt + 1
    return amt

first = calculate(1,1)
second = calculate(3,1)
third = calculate(5,1)
fourth = calculate(7,1)
fifth = calculate(1,2)

print(first * second * third * fourth * fifth)
