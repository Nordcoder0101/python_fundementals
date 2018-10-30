def biggieSize(list):
    for i in list:
    # for i in range(0, len(list), 1):
      if list[i] > 0:
        list[i] = 0
    print(list)


def countPositives(list):
    count = 0
    for i in range(0, len(list), 1):
        if list[i] > 0:
            count += 1
    list[len(list)-1] = count
    print(list)

def sumTotal(list):
    sum = 0
    for i in range(0, len(list), 1):
        sum += list[i]
    return sum    

def average(list):
    sum = 0
    for i in range(0, len(list), 1):
        sum += list[i]
    average = (sum / len(list))
    print(sum, len(list))
    print(average)

def length(list):
    length = len(list)
    print(length)

def minimum(list):
    if len(list) == 0:
        return 0
    minVal = list[0]
    
    for i in range(0, len(list)):
        if list[i] < minVal:
            minVal = list[i]
    return minVal


def maximum(list):
    if len(list) == 0:
        return False
    max = list[0]
    for i in range(0, len(list)):
        if list[i] > max:
            max = list[i]
    print(max)

def ultimateAnalysis(list):
    my_dict = {"sumTotal": 0, "average": 0, "minimum": list[0], "maximum": list[0], "length": len(list)}
    for i in range(0, len(list)):
        my_dict["sumTotal"] += list[i]
        if list[i] > my_dict["maximum"]:
            my_dict["maximum"] = list[i]
        if list[i] < my_dict["minimum"]:
            my_dict["minimum"] = list[i]
    my_dict["average"] = (my_dict["sumTotal"] / my_dict["length"])
    print(my_dict)

def reverseList(list):
    temp = 0
    for i in range(0, round((len(list)/2)), 1):
        temp = list[i]
        list[i] = list[len(list) - 1 -i]
        list[len(list) - 1 - i] = temp
        
    print(list)    


