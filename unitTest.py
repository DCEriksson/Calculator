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

lst = ['12', '/', '6']
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
