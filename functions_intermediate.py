import random
def randInt(min=50, max=100):
  
    if max == None and min == None:
        num = random.random() * 100
        return num
    elif max and min == None:
        num = random.random() * max
        return num
    elif max == None and min:
        num = random.random() * min + 50
        return num
    else:
        num = random.random() * max
        print(num)
        return num

randInt()