                    # PYTHON LIST POP METHOD
                    
# In this tutorial, we will learn about the Python List pop() method with the help of examples.
# The pop() method removes the item at the given index from the list and returns the removed item.

# Example
# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# remove the element at index 2
removed_element = prime_numbers.pop(2)

print('Removed Element:', removed_element) # Removed Element: 5
print('Updated List:', prime_numbers) # Updated List: [2, 3, 7]

# The syntax of the pop() method is: list.pop(index)
# pop() parameters
# The pop() method takes a single argument (index).
# The argument passed to the method is optional. If not passed, the default index -1 is passed as an argument (index of the last item).
# If the index passed to the method is not in range, it throws IndexError: pop index out of range exception.
# Return Value from pop()
# The pop() method returns the item present at the given index. This item is also removed from the list.

# Example 1: Pop item at the given index from the list
# programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']

# remove and return the 4th item
return_value = languages.pop(3)

print('Return Value:', return_value) # Return Value: French

# Updated List
print('Updated List:', languages) # Updated List: ['Python', 'Java', 'C++', 'C']

# Note: Index in Python starts from 0, not 1.
#If you need to pop the 4th element, you need to pass 3 to the pop() method.

# Example 2: pop() without an index, and for negative indices
# programming languages list
languages = ['Python', 'Java', 'C++', 'Ruby', 'C']

# remove and return the last item
print('When index is not passed:') # When index is not passed:
print('Return Value:', languages.pop()) # Return Value: C

print('Updated List:', languages) # Updated List: ['Python', 'Java', 'C++', 'Ruby']

# remove and return the last item
print('\nWhen -1 is passed:') # When -1 is passed:
print('Return Value:', languages.pop(-1)) # Return Value: Ruby

print('Updated List:', languages) # Updated List: ['Python', 'Java', 'C++']

# remove and return the third last item
print('\nWhen -3 is passed:') # When -3 is passed:
print('Return Value:', languages.pop(-3)) # Return Value: Python

print('Updated List:', languages) # Updated List: ['Java', 'C++']

# If you need to remove the given item from the list, you can use the remove() method.

                    # PYTHON LIST REMOVE METHOD
                    
# In this tutorial, we will learn about the Python List remove() method with the help of examples.
# The remove() method removes the first matching element (which is passed as an argument) from the list.

# Example
# create a list
prime_numbers = [2, 3, 5, 7, 9, 11]

# remove 9 from the list
prime_numbers.remove(9)

# Updated prime_numbers List
print('Updated List: ', prime_numbers) # Updated List:  [2, 3, 5, 7, 11]

# The syntax of the remove() method is: list.remove(element)
# remove() Parameters
# The remove() method takes a single element as an argument and removes it from the list.
# If the element doesn't exist, it throws ValueError: list.remove(x): x not in list exception.
# Return Value from remove()
# The remove() doesn't return any value (returns None).

# Example 1: Remove element from the list
# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']

# 'rabbit' is removed
animals.remove('rabbit')

# Updated animals List
print('Updated animals list: ', animals) # Updated animals list:  ['cat', 'dog', 'guinea pig']

# Example 2: remove() method on a list having duplicate elements
# If a list contains duplicate elements, the remove() method only removes the first matching element.

# animals list
animals = ['cat', 'dog', 'dog', 'guinea pig', 'dog']

# 'dog' is removed
animals.remove('dog')

# Updated animals list
print('Updated animals list: ', animals) # Updated animals list:  ['cat', 'dog', 'guinea pig', 'dog']
# Here, only the first occurrence of element 'dog' is removed from the list.

# Example 3: Deleting element that doesn't exist
# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']

# Deleting 'fish' element
animals.remove('fish')

# Updated animals List
print('Updated animals list: ', animals)

# OUTPUT
# Traceback (most recent call last):
#  File ".. .. ..", line 5, in <module>
#    animal.remove('fish')
# ValueError: list.remove(x): x not in list

# Here, we are getting an error because the animals list doesn't contain 'fish'.

                    # PYTHON LIST CLEAR METHOD

# In this tutorial, we will learn about the Python List clear() method with the help of examples.
# The clear() method removes all items from the list.

# Example
prime_numbers = [2, 3, 5, 7, 9, 11]

# remove all elements
prime_numbers.clear()

# Updated prime_numbers List
print('List after clear():', prime_numbers) # List after clear(): []

# The syntax of clear() method is: list.clear()

# clear() Parameters
# The clear() method doesn't take any parameters.

#Return Value from clear()
#The clear() method only empties the given list. It doesn't return any value.

#Example 1: Working of clear() method
# Defining a list
list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
list.clear()

print('List:', list) # List: []
#Note: If you are using Python 2 or Python 3.2 and below, you cannot use the clear() method. You can use the del operator instead.

#Example 2: Emptying the List Using del
# Defining a list
list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
del list[:]

print('List:', list) # List: []
