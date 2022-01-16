# PYTHON REVERSED METHOD

#The reverse() method reverses the elements of the list.
#Example
# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# reverse the order of list elements
prime_numbers.reverse()


print('Reversed List:', prime_numbers)# Output: Reversed List: [7, 5, 3, 2]

# The syntax of the reverse() method is:list.reverse()
# reverse() parameter
# The reverse() method doesn't take any arguments.

# Return Value from reverse()
# The reverse() method doesn't return any value. It updates the existing list.

#Example 1: Reverse a List
# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems) # Original List: ['Windows', 'macOS', 'Linux']

# List Reverse
systems.reverse()


# updated list
print('Updated List:', systems) # Updated List: ['Linux', 'macOS', 'Windows']

#There are other several ways to reverse a list.

#Example 2: Reverse a List Using Slicing Operator
# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems) # Original List: ['Windows', 'macOS', 'Linux']

# Reversing a list	
# Syntax: reversed_list = systems[start:stop:step] 
reversed_list = systems[::-1]

# updated list
print('Updated List:', reversed_list) # Updated List: ['Linux', 'macOS', 'Windows']

# Example 3: Accessing Elements in Reversed Order
# If you need to access individual elements of a list in the reverse order, it's better to use the reversed() function.

# Operating System List
systems = ['Windows', 'macOS', 'Linux']

# Printing Elements in Reversed Order
for o in reversed(systems):
    print(o)
# Output:
#       Linux
#       macOS
#       Windows