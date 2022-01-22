# Little bit review for mutible and immutiable
# String variables are immutiable means that after applying methods 
# our variable will nnot change but for mutiable ones it will change
# the variable

# EXAMPLE

string_value = "tommy"
list_value = ['t', 'o', 'm']
print("First: ", string_value)
print("First: ", list_value, type(list_value))
string_value.upper()
print('string_value.upper() result: ', string_value.upper())
list_value.sort()
print("Second: ", string_value)
print("Second: ", list_value)

# Description
# The index() method returns the lowest index in list that obj appears.

# Syntax for index() method − list.index(obj)
# Parameters obj − This is the object to be find out.

# Return Value
# This method returns index of the found object otherwise raise 
# an exception indicating that value does not find.

#Example
#The following example shows the usage of index() method.

#Live Demo
#!/usr/bin/python3

list1 = ['physics', 'chemistry', 'maths']
print ('Index of chemistry', list1.index('chemistry'))
print ('Index of C#', list1.index('C#'))
