inp = open('InputData.txt').read().split('\n')

def validatePassword(lowestRate, highestRate, keyword, password):
    # print(password.count(keyword), keyword)
    if password.count(keyword) >= lowestRate and password.count(keyword) <= highestRate:
        return True
    return False

amt = 0
for x in range(len(inp)):
    entries = inp[x].split(' ')
    lowestRate = int(entries[0].split('-')[0])
    highestRate = int(entries[0].split('-')[1])
    keyword = str(entries[1].split(':')[0])
    password = entries[2]
    validated = validatePassword(lowestRate,highestRate,keyword,password)
    if validated == True:
        amt += 1

print(amt)