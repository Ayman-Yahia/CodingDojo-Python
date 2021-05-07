import random
def randInt(min=0, max=100):
    if min > max:
        print("please choose a min number that is less than max")
        return
    elif max < 0:
        print("please choose a positive number for max")
        return 
    Num = random.random() * (max - min) + min
    return round(Num)
