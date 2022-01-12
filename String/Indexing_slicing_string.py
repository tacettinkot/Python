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