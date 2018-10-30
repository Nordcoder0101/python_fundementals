def countdown(num):
    list = []
    for i in range(num, -1, -1):
        list.append(i)
        
    print(list)

def printAndReturn(list):
    print(list[0])
    return list[1]

def firstPlusLength(list):
    sum = 0
    sum += list[0]
    sum += len(list)
    print(sum)


def greaterThanSecond(list):
    newList = []
    valueToCompare = list[1]
    count = 0
    for i in list:
        if i > valueToCompare:
            newList.append(i)
            count = count + 1
    if len(newList) >= 2:
        print(count)
        return newList
    else:
        return False    
    
def thisLengthThatValue(size, value):
    list = []
    for i in range(0,size):
        list.append(value)
    print(list)    

   