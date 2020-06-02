for x in range(0, 150, 1):
    print(x)

for x in range(5,1000,5):
    print(x)

total= 0
for x in range(1,101,1):
    if x % 10 == 0:
        print("CodingDojo")
    elif x % 5 == 0:
        print("Dojo") 
    else:
        print(x)

total = 0
for x in range(500000):
    if x % 2 != 0:
        total += x
print(total)

for x in range(2018,0,-4):
    print(x)

lowNum= 3
highNum= 63
mul= 4 
for x in range(lowNum, highNum):
    if x % mul == 0:   
        print(x, end=" ")