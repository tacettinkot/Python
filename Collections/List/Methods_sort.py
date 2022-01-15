# PYTHON SORT METHOD

# The sort() method sorts the elements of a given list in a specific ascending or descending order.

#Example
prime_numbers = [11, 3, 7, 5, 2]

# sort the list
prime_numbers.sort()
print(prime_numbers) # [2, 3, 5, 7, 11]

# The syntax of the sort() method is: list.sort(key=..., reverse=...)
# Alternatively, you can also use Python's built-in sorted() function for the same purpose.

sorted(list, key=..., reverse=...)
# Note: The simplest difference between sort() and sorted() is: sort() changes the list directly 
# and doesn't return any value, while sorted() doesn't change the list and returns the sorted list.

# sort() Parameters
# By default, sort() doesn't require any extra parameters. However, it has two optional parameters:

# reverse - If True, the sorted list is reversed (or sorted in Descending order)
# key - function that serves as a key for the sort comparison
# sort() Return Value
# The sort() method doesn't return any value. Rather, it changes the original list.

# If you want a function to return the sorted list rather than change the original list, use sorted().

# Example 1: Sort a given list
# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort()

# print vowels
print('Sorted list:', vowels) # Sorted list: ['a', 'e', 'i', 'o', 'u']

# Sort in Descending order
# The sort() method accepts a reverse parameter as an optional argument.

# Setting reverse = True sorts the list in the descending order.

# list.sort(reverse=True)
# Alternatively for sorted(), you can use the following code.

sorted(list, reverse=True)
# Example 2: Sort the list in Descending order
# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort(reverse=True)

# print vowels
print('Sorted list (in Descending):', vowels) # Sorted list (in Descending): ['u', 'o', 'i', 'e', 'a']

#Sort with custom function using key
#If you want your own implementation for sorting, the sort() method also accepts a key function as an optional parameter.

#Based on the results of the key function, you can sort the given list.

list.sort(key=len)
# Alternatively for sorted:

sorted(list, key=len)

# Here, len is Python's in-built function to count the length of an element.

# The list is sorted based on the length of each element, from lowest count to highest.

# We know that a tuple is sorted using its first parameter by default. Let's look at how to customize the sort() method to sort using the second element.

# Example 3: Sort the list using key
# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
random.sort(key=takeSecond)

# print list
print('Sorted list:', random) # Sorted list: [(4, 1), (2, 2), (1, 3), (3, 4)]
# Let's take another example. Suppose we have a list of information about the employees of an office where each element is a dictionary.
# We can sort the list in the following way:

# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# custom functions to get employee info
def get_name(employee):
    return employee.get('Name')

def get_age(employee):
    return employee.get('age')

def get_salary(employee):
    return employee.get('salary')

# sort by name (Ascending order)
employees.sort(key=get_name)
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=get_age)
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=get_salary, reverse=True)
print(employees, end='\n\n')

[{'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'John Hopkins', 'age': 18, 'salary': 1000}, {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}]

[{'Name': 'John Hopkins', 'age': 18, 'salary': 1000}, {'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}, {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}]

[{'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}, {'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}, {'Name': 'John Hopkins', 'age': 18, 'salary': 1000}]
# Here, for the first case, our custom function returns the name of each employee. 
# Since the name is a string, Python by default sorts it using the alphabetical order.

# For the second case, age (int) is returned and is sorted in ascending order.

# For the third case, the function returns the salary (int), and is sorted in the descending order using reverse = True.

# It is a good practice to use the lambda function when the function can be summarized in one line. 
# So, we can also write the above program as:

# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# sort by name (Ascending order)
employees.sort(key=lambda x: x.get('Name'))
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=lambda x: x.get('age'))
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=lambda x: x.get('salary'), reverse=True)
print(employees, end='\n\n')
Output

[{'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'John Hopkins', 'age': 18, 'salary': 1000}, {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}]

[{'Name': 'John Hopkins', 'age': 18, 'salary': 1000}, {'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}, {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}]

[{'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}, {'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}, {'Name': 'John Hopkins', 'age': 18, 'salary': 1000}] 