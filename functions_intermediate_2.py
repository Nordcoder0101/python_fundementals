x = [ [5,2,3], [10,8,9]]
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

sports_dictionary = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 20} ]

# for i in range(0,len(x)):
#   for j in range(0, len(x[i])):
#     if x[i][j] == 10:
#         x[i][j] = 15

# students[0]['last_name'] = 'Bryant'

# sports_dictionary['soccer'][0] = 'Andres'

# print(sports_dictionary)

# z[0]['y'] = 30

# print(z)

def iterateStudents(list):
  for i in range(0, len(list)):
          print(list[i])



def iterateDictionary2(key_name, some_list):
    for i in range(0, len(some_list)):
        for k in some_list[i]:
            if k == key_name:
                print(some_list[i][k])



dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(some_dict):
    for k in some_dict:
        print(len(some_dict[k]), k)
        for i in range(0, len(some_dict[k])):
            print(some_dict[k][i])     

print_info(dojo)