def seperatorList(mathStr):
    mathList = []
    tempStr = mathStr[0]
    for i in mathStr[1:]:
        if i.isnumeric():
            tempStr += i
        else:
            mathList.append(tempStr)
            mathList.extend(i)
            tempStr = ""
    mathList.append(tempStr)
    return mathList

def multiplication(lst):
    numberOfMulti = lst.count('*')
    for _ in range(numberOfMulti):
        index = lst.index('*')
        tempVal = int(lst[index-1]) * int(lst[index+1])
        lst.pop(index+1)
        lst.pop(index)
        lst.pop(index-1)
        lst.insert(index-1, str(tempVal))
    return lst

def division(lst):
    numberOfDivis = lst.count('/')
    for _ in range(numberOfDivis):
        index = lst.index('/')
        tempVal = int(lst[index-1]) / int(lst[index+1])
        lst.pop(index+1)
        lst.pop(index)
        lst.pop(index-1)
        lst.insert(index-1, str(tempVal))
    return lst

x = "12/6"
tempList = seperatorList(x)
if tempList.count('*'):
    tempList = multiplication(tempList)
if tempList.count('/'):
    tempList = division(tempList)
if tempList.count('+') or tempList.count('-'):
    summation = int(tempList[0])
    for i in range(1, len(tempList), 2):
        if tempList[i] == '+':
            summation += int(tempList[i+1])
        if tempList[i] == '-':
            summation -= int(tempList[i+1])
    print(summation)
else:
    print(tempList[0])

