#!/usr/bin/python

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


#print (dict['one'] )      # Prints value for 'one' key
#print (dict[2]  )         # Prints value for 2 key
print (tinydict )         # Prints complete dictionary
print (tinydict.keys() )  # Prints all the keys
print (tinydict.values()) # Prints all the values

print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
print ("dict['Class']: ", dict['Class'])

dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry

print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
print ("dict['Class']: ", dict['Class'])
print ("dict['School']: ", dict['School'])


people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people)

print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])

people[3] = {}

people[3]['name'] = 'Luna'
people[3]['age'] = '24'
people[3]['sex'] = 'Female'
people[3]['married'] = 'No'

print(people[3])

people[4] = {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}
print(people[4])

del people[3]['married']
del people[4]['married']

print(people[3])
print(people[4])

print(people)
del people[3], people[4]
print(people)

for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)

    for key in p_info:
        print(key + ':', p_info[key])


var = 100
if ( var == 100 ) : print ("Value of expression is 100")
print ("Good bye!")