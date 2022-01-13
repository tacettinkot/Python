              # PYTHON LIST APPEND METHOD

# In this tutorial, we will learn about the Python list append() method with the help of examples.
# The append() method adds an item to the end of the list.

# Example
currencies = ['Dollar', 'Euro', 'Pound']

# append 'Yen' to the list
currencies.append('Yen')
print(currencies) # Output: ['Dollar', 'Euro', 'Pound', 'Yen']

# The syntax of the append() method is: list.append(item)
# append() Parameters
# The method takes a single argument

# item - an item (number, string, list etc.) to be added at the end of the list
# Return Value from append()
# The method doesn't return any value (returns None).

# Example 1: Adding Element to a List
# animals list
animals = ['cat', 'dog', 'rabbit']

# Add 'guinea pig' to the list
animals.append('guinea pig')

print('Updated animals list: ', animals) # animals list:  ['cat', 'dog', 'rabbit', 'guinea pig']

#Example 2: Adding List to a List
# animals list
animals = ['cat', 'dog', 'rabbit']

# list of wild animals
wild_animals = ['tiger', 'fox']

# appending wild_animals list to animals
animals.append(wild_animals)

print('Updated animals list: ', animals) # Updated animals list:  ['cat', 'dog', 'rabbit', ['tiger', 'fox']]

#In the program, a single item (wild_animals list) is added to the animals list.

             # PYTHON LIST INSERT METHOD
             
# In this tutorial, we will learn about the Python List insert() method with the help of examples.
# The insert() method inserts an element to the list at the specified index.

# Example
# create a list of vowels
vowel = ['a', 'e', 'i', 'u']

# 'o' is inserted at index 3 (4th position)
vowel.insert(3, 'o')

print('List:', vowel) # Output: List: ['a', 'e', 'i', 'o', 'u']

# The syntax of the insert() method is : list.insert(i, elem)
# Here, elem is inserted to the list at the ith index. All the elements after elem are shifted to the right.

# insert() Parameters
# The insert() method takes two parameters:

# index - the index where the element needs to be inserted
# element - this is the element to be inserted in the list
# Notes:

# If index is 0, the element is inserted at the beginning of the list.
# If index is 3, the index of the inserted element will be 3 (4th element in the list).
# Return Value from insert()
# The insert() method doesn't return anything; returns None. It only updates the current list.

# Example 1: Inserting an Element to the List
# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# insert 11 at index 4
prime_numbers.insert(4, 11)

print('List:', prime_numbers) # List: [2, 3, 5, 7, 11]

# Example 2: Inserting a Tuple (as an Element) to the List
mixed_list = [{1, 2}, [5, 6, 7]]

# number tuple
number_tuple = (3, 4)

# inserting a tuple to the list
mixed_list.insert(1, number_tuple)


print('Updated List:', mixed_list) # Updated List: [{1, 2}, (3, 4), [5, 6, 7]]

