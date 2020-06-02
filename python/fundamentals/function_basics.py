#1 
def countdown (num):
    newArr = []
    for i in range(num,-1,-1):
        newArr.append(i)
        
    return newArr

print(countdown(6))

#2
def print_and_return (x):
    print(x[0])
    return(x[1])

print(print_and_return([1,2,3,4]))

#3
def first_plus_length(x):
    sum= x[0] +len(x)
    return sum
print(first_plus_length([1,2,3,4,5,6]))

#4
def values_greater(x):
    newArr=[]
    if len(x)<2:
        return False
    else:
        for i in range(0,len(x),1):
            if x[1]< x[i]:
                newArr.append(x[i])
        return newArr

print(values_greater([1]))
print(values_greater([5,4,2,3,1,6,55,5]))

#5
def len_and_val(x,y):
    newArr=[]
    for i in range(0,x):
        newArr.append(y)
    return newArr

print(len_and_val(10 ,9))
    

