# String Formatting with f-string
# The formula syntax 👇

# f'string {variable1} string {variable2} string'

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
