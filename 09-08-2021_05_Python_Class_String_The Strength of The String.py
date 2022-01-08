# The Strength of The String
my_name = 'Taji'
print(my_name)
print('=======1) Indexing&Slicing Strings======')
# 1) Indexing&Slicing Strings
# It will allow us to seperate the string in its characters
# [start:stop:step]
# [0:last index: 1] by default value

city = 'Phoenix'

print(city[1:]) # Starts from index 1 to the end
print(city[:6]) # Starts from index zero to 5th index
print(city[::2]) # Starts from index zero to the end by 2 step
print(city[1::2]) # Starts from index 1 to the end by 2 step
print(city[-3:]) # Starts from index -3 to the end
print(city[::-1]) # negative step starts from the end to zero
print('===== Different example====')
print(city[-2:-6:-2])
print(city[-1:-5:2],' 2nd line')
print(city[-2:-6],' 3rd line')# gives empty space beacuse of wrong index follow

# Negative indexing works as the same
'  O r a n g e'
# -6-5-4-3-2-1
# Last isndex is always -1
# len() function measure the length of any iterable:

vegetable = 'Tomato'
print('The length of the word', vegetable, 'is :' , len(vegetable))
print('====== 2) String Formatting with Arithmetic Syntax ==============')
# 2) String Formatting with Arithmetic Syntax
# We can use arithmetic operator syntaxes in string formatting operations
# Here are basic operators : +,=,*

# + ==> is concatination means add to stings together
# = ==> is assigment
# * ==> is define how many times same string will repeat
str_one = 'upper'
str_two = 'case'
str_comb = str_one + str_two
print(str_comb)
print(3 * str_comb)
print(* str_one)

# Ex: Separate these strings into its characters using *
string1 = 'I am angry'
'alex@clarusway.com'

print(* string1)
print(* 'alex@clarusway.com')

str_one += str_two
str_two *= 3
print(str_one, str_two)
str_one = 'upper'
str_two = 'case'
print('====== 3) string.format() =========')
# 3) string.format()
# String Formatting with string.format() Method
# The formula syntax 👇

#print('string {} string {} string'.format(data1, data2))

print('My favourite school is {}. I learn {} in it!'.format('Clarusway','Python'))

fruit = 'Orange'
amount = 4
print('The amount of {} we bought is {} pounds'.format(fruit,amount))

print('{state} is most {adjective} state'.format(state='California',adjective='crowded'))

print("{1}'s daugter name is {0}. She is {age} years old".format("Alya","Tacettin",age=3))

print('====== 4) String Formatting with f-string ====')
#4) String Formatting with f-string
#The formula syntax 👇

#f'string {variable1} string {variable2} string'

fruit = 'Orange'
amount = 4
vegetable = 'Apple'
output = f"The amount of {fruit} and {vegetable} we bought are totally {amount} pounds."
print(output)

# You can use all valid expressions, variables, and even methods in curly braces.
sample = f"{2 ** 3}"
print(sample)

# Task :
# ▹ Type a Python code to get the output of “My name is Mariam”, 
# using .capitalize() and f-string methods with the name variable below.
name = "MARIAM"
print(f'My name is {name.capitalize()}')

# There is also a multiline f-string formatting style. 👇

name = 'Taji'
job = 'teachers'
domain = 'DevOps'
message = (
    f'Hi {name}, '
    f'You are one of the {job} '
    f'in the {domain} section.'
) # while using multiline be careful about () or \
print(message)

# message = f'Hi {name}, ' \
#     f'You are one of the {job} '\
#     f'in the {domain} section.'
