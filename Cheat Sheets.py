
# LISTS - stores a series of items in a particular order.

# initialization
bikes = ['trek', 'redline', 'giant']

# get the last element in a list
last_bike = bikes[-1]
last_bike

# making numerical lists (example 1)
squares = []
for x in range(1, 11):
    squares.append(x**2)
squares

# list comprehensine (example 2)
squares = [x**2 for x in range(1,11)]
squares

# copying list
bikes_copy = bikes[:]
bikes_copy

# Modifying an element in the list
bikes_copy[1] = 'new bike'
bikes_copy

# Adding an element to the end of the list
bikes_copy.append('appended element')
bikes_copy

# Inserting an element to the particular position
bikes_copy.insert(0, 'inserted element')
bikes_copy

# Delete an element by its position
del bikes_copy[0]
bikes_copy

# Remove an element from list
bikes_copy.remove('giant')

# 'pop' function helps to work with the removed element
# if you think the list of items as a stack, it gets element from the top of the list
el  = bikes_copy.pop()

# pop the element based on the index
el = bikes_copy.pop(2)

# list length
length = len(bikes_copy)
length

# Sorting a list
#  1. sort() - it changes the order of a list permanenetly. 
#  2. sorted() - it returns a copy of the list and living the original list uncanged.
# NOTE: lowercasde and uppercase letters may affect the sort order.

# sort the list permanently 
bikes_copy.sort()

# get the sorted copy of the list
bikes_sorted = sorted(bikes_copy)

# sorting the list permanently in reverse alphabetical order
bikes_copy.sort(reverse=True)

# reversing the order of a list
bikes_copy.reverse()

# Looping through a list
for bike in bikes_copy:
    print(bike)

# making the list of numbers from 1 to n
n = 10
numbers = list(range(1, n+1))

# find mininum value in a list
print(min(numbers))

# find maximum value in a list
print(max(numbers))

# find sum of all values in a list
print(sum(numbers))

# Slicing a list
# getting first k items from the list
k = 4
first_k = numbers[:k]

# getting last k items from the list
last_k = numbers[-k:]

# getting the items between given two indexes from the list
between = numbers[1:k]

# Testing if a value is in a list
if('trek' in bikes_copy):
    print('Yes, the given element exists in the list')
elif('trek' not in bikes_copy):
    print('No, the element doesnt exist')
    
# Checking if the list empty
if(bikes_copy):
    print('The list is not empty ...')


# Tuples - similar to the lists, but the items in a tuple can't be modified
dimensions = (1920, 1080)
dimensions


# Dictationaries - sotres items, and each item is a key-value pair

# initialization
dict_sample = {'val1':10, 'val2':15}

# looping hrough all key-value pairs
for val, number in dict_sample.items():
    print(val, number)
    
# looping through all keys
for val in dict_sample.keys():
    print(val)
    
# looping through all values
for number in dict_sample.values():
    print(number)
    
# Accessing values
print(dict_sample['val1'])

# NOTE: if the key doesn't exist it will give an error.
# to avoid this kind of issue, it is we can use get() function
# if the key doesnt exist, it will return None
# we could define a default value inside get() function
print(dict_sample.get('val3', 20))

# Deleting a key-value pair
del dict_sample['val2']

# Functions

# default values for parameters
def function1(var=15):
    print("value is ",var)
    
function1()
function1(20)

# Positional and keyword arguments
# 2 kinds of arguments: Positional, Keyword
# Positional: python matches the first argument in the function with the first parameter in the function definition
# Keyword: you specify which parameter each argument should be assigned in the function call. The order no matters

# Using positional
def pos_function(arg1, arg2):
    print("Positional: argument 1 is "+str(arg1)+" argument 2 is "+str(arg2))

pos_function(1, 2)

# Using keyword
def key_function(arg1, arg2):
    print("Keyword: argument 1 is "+str(arg1)+" argument 2 is "+str(arg2))

key_function(arg2 = 3, arg1 = 4)

# Default values
# you ca provide default value for a parameter. 
# when function calls omit this argument, the default value will be used
def def_value(arg1, arg2='2'):
    print("Default: argument 1 is "+arg1+" argument 2 is "+arg2)

def_value('1')

# Using none to mnake an argument optional
def none_value(arg1, arg2=None):
    if(arg2):
        print("None: argument 1 is "+arg1+" argument 2 is "+arg2)
    else:
        print("None: argument 1 is "+arg1)
        
none_value('a', 'b')
none_value('a')


# Passing an arbitrary number of arguments
# sometimes it is hard to predict the number of arguments we need
# * operator helps to specify the arbitrary arguments (it must come last in the function definition)
# ** operator allows a parameter to collect arbitrary number of keyword arguments

def find_maths(rule, *numbers):
    answer = 0;
    if(rule is 'sum'):
        for number in numbers:
            answer = answer+number
    return answer

def build_dict(first, last, **user_info):
    # build a dict with therequired keys
    profile = {'first':first, 'last':last}
    
    # add any other keys and values
    for key, value in user_info.items():
        profile[key] = value
    
    return profile

# * operator function result
answer = find_maths('sum', 1, 2, 3)
user = build_dict('albert', 'einstein', location='princeton')

print(answer)
print(user)


# Classes
# creating class
class Animal():
    # constructor
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def getName(self):
        return self.name
    
    def getHeight(self):
        return self.height

# creating object
animal = Animal('rosie', 100)

# accessing attributes
print(animal.name);
print(animal.height)

# modifying attributes
# this can be achieved trough the object attribute or creating setter method
animal.name = 'rex'
print("new animal name is "+animal.name)


# Class Inheritance
# when using inheritance: if the class is the specialized version of another class, you can use inheritance.
# it can take the parent classes attributes
# sub class can create new attributes and methods and even override them of parent class
class Specie(Animal):
    def __init__(self, name, height, specie):
        super().__init__(name, height)
        
        # classes own attribute
        self.specie = specie

specie = Specie('Rose', 1500, 'horse')
print("New animal specie details: "+specie.specie)

# Instance as attributes
# a class can have objects as attributes
class Issue():
    def __init__(self, desc, problem):
        self.desc = desc
        self.problem = problem
    
    def getDesc(self):
        return self.desc
    
class Data():
    def __init__(self):
        self.issue = Issue('description', 'problem')

data = Data()
desc = data.issue.getDesc()
print(desc)

# Files

# Read file and store its lines
filename = 'example.txt'
with open(filename) as file:
    lines = file.readlines() # returns an array of lines
    
for line in lines:
    print(line)
    
# Writing to a file
with open(filename, 'w') as file:
    file.write('writing to a file')
    
# Appending to a file
with open(filename, 'a') as file:
    file.write('\nappending to file')


# Exceptions - help you to respond users when errors that occur

# Catching exception

a = 'a';

try:
    num = int(a)
except ValueError:
    print('Looks like the value is not an integer')
else:
    print('The number is ',a)

