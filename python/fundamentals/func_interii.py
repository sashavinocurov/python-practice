x = [ [5,10,2,3], [10,8,9,10,3,5,10] ] 
def change_var(x):
    # x[1].pop(0)
    # x[1].insert(0, 15)
    # x[1][0] = 15
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] == 10:
                x[i][j] = 15
    return x

print(change_var(x))

def a(alist):
    for item in alist:
        do_something(item)

    for i in range(len(alist)):
        do_something(item)

    alist = [1]
    len(alist) == 1
    index == 0
    i = 0
    l = len(alist)
    while i < l:
        item = alist[i]
        do_something(item)
        i += 1

    j = 0
    while True:
        item = alist[j]
        # j += 1
        if j == len(alist):
            break

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
def chang_last (students):
   students[0]['last_name'] = "Bryant"
   return students

print(chang_last(students))
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
def soccer_change(sports_directory):
    sports_directory['soccer'][0]= "Andres"
    return sports_directory

print(soccer_change(sports_directory))

z = [ {'x': 10, 'y': 20} ]
def change_num(x):
    z[0]['y'] = 30
    return z

print(change_num(z))

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for i in range(len(students)):
        print('First Name-',students[i]["first_name"],'Last Name-',students[i]["last_name"])

iterateDictionary(students)

def iterateDictionary2(students):
    for i in range(len(students)):
        print(students[i]['first_name'])

iterateDictionary2(students)

def iterateDictionary3(students):
    for i in range(len(students)):
        print(students[i]['last_name'])

iterateDictionary3(students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(dojo):
    # print(len(dojo['locations']),'Locations')
    for i in range(len('locations')):
        print(dojo['locations'][i])

    # print(len(dojo['instructors']),'Instractors')
    for k in range(len('instructors')):
        print(dojo['instructors'][k])

# printInfo(dojo)
def printInfo(dojo):
    for i in dojo:
        print(len(dict[i]),i)
        for j in dojo:
            print(len(dict[j]),j)

printInfo(dojo)