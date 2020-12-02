inp = open('input01.txt').read().split('\n')

def validatePassword(lowestRate, highestRate, keyword, password):
    if password[lowestRate] == keyword:
        if password[lowestRate] == keyword and password[highestRate] == keyword:
            return False
        else:
            return True
    elif password[highestRate] == keyword:
        return True
    return False

amt = 0
for x in range(len(inp)):
    entries = inp[x].split(' ')
    lowestRate = int(entries[0].split('-')[0]) - 1
    highestRate = int(entries[0].split('-')[1]) - 1
    keyword = str(entries[1].split(':')[0])
    password = entries[2]
    validated = validatePassword(lowestRate,highestRate,keyword,password)
    if validated == True:
        amt += 1

print(amt)