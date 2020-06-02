# #1 
# def biggie(x):
#     newArr=[]
#     for i in range(len(x)):
#         if x[i]>= 0:
#             newArr.append("Big")
#         else:
#             newArr.append(x[i])
#     return newArr

# print(biggie([-1,-4,5,-3,2,1,-1,0]))

# 2
# def count_pos(x):
#     counter = 0
#     for i in range(len(x)):
#         if x[i]>0:
#             counter += 1
#     x[len(x)-1]=counter
#     print(x)

# count_pos([-1,2,3,-1,2,-1])

# #3
# def su_num(x):
#     sum=0
#     for i in range (len(x)):
#         sum += x[i]
#     return sum

# print(su_num([2,2,3,4,5,6,7]))


# 4
# def average (x):
#     ave= 0
#     sum= 0
#     for i in range (len(x)):
#         sum += x[i]
#         ave= sum / len(x)
#     print(ave)

# average([1,2,3,4,5])

# #5
# def length (x):
#     leng = 0
#     for i in range (len(x)):
#         leng += 1
#     return leng

# print(length([12,24,5,23]))

# #6
# def minimum (x):
#     min=x[0]
#     for i in x:
#         if i < min:
#             min=i
#     return min

# print(minimum([5,23,-12,0,15]))

# #7
# def maximum (x):
#     max=x[0]
#     for i in x:
#         if i > max:
#             max=i
#     return max

# print(maximum([5,23,-12,0,15]))

# #8
# def ultimate (x):
#     min= x[0]
#     max= x[0]
#     sum= 0
#     for i in range(len(x)):
#         if i > max:
#             max=i
#         elif i < min:
#             min=i
#         sum += x[i]
#         ave= sum / len(x)
#     dict = {"minimum": min, "maximum": max, "sumTotal": sum, "average": ave, "length": len(x)} 
#     print (dict)

# ultimate([5,23,-12,0,15])  

# 9
# def reverse (x):
#     newArr=[]
#     for i in range(len(x)-1, -1, -1):
#         newArr.append(x[i])
#     return newArr

# print(reverse([1,2,3,4,5]))

def removeDubs(x):
    for i in range(len(x)):
        # temp = x[i]
        for j in range(len(x)-1, i, -1):
            if x[i] == x[j]:
                x.pop(j)
            else:
                continue
    return x

print(removeDubs([1,1,3,5,2,3,1]))
