def show_changes(list1):
    for item in list1: print(item)
    print(' ')

# 1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30

show_changes([x,students, sports_directory, z])
print(' ')

# 2. Iterate Through a List of Dictionaries
students = [{'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}]
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary(list1):
    for dict1 in list1:
        print(f"first_name - {dict1['first_name']}, last_name - {dict1['last_name']}")

iterateDictionary(students) 
print(' ')

# 3. Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for dict1 in some_list:
        print(dict1[key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)
print(' ')

# 4. Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for key in some_dict.keys():
        print(str(len(some_dict[key])) + ' ' + key)
        for item in some_dict[key]: print(item)
        print(' ')

dojo = {'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']}

printInfo(dojo)
print(' ')