

def power(num, pwr):
    if pwr == 0:
        return 1
    else: 
        return num * power(num, pwr-1)


def factoria(num):
    if num == 0:
        return 1
    else: 
        return num * factoria(num - 1)


print("{} to the power or {} is {}".format(5, 3, power(5, 3)))
print("{} to the power of {} is {}".format(1, 5, power(1, 5)))
print("{}! is {}". format(4, factoria(4)))
print("{}! is {}". format(0, factoria(0)))