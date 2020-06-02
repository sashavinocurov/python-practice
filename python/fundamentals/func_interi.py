import random
def randint(min=0,max=100):
    num = random.random()*(max-min)+min
    if min>max:
        print("number to low")
        return False
    elif max<0:
        print("number is 0")
        return False
    print(round(num))

randint(-1, -1)


