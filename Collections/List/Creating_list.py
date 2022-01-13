# [] and list() create list collection

# Example
"veli" # str variable 
list("veli") # ['v', 'e', 'l', 'i']
str = "ali"
print(list(str)) # ['a', 'l', 'i']

# str variable splits into its chracters and stored in list
# But if we put into [] then it will accept as an one variable

# Example
l = ["ali"] 
print(l) #  ['ali']

list_1 = ['h', 'a', 'p', 'p', 'y']
word = "happy"
list_2 = list(word)

print(list_1) # ['h', 'a', 'p', 'p', 'y']
print(list_2) # ['h', 'a', 'p', 'p', 'y']

country =['USA', 'Brasil', 'UK', 'Germany', 'Turkey', 'New Zealand']
print(country) # ['USA', 'Brasil', 'UK', 'Germany', 'Turkey', 'New Zealand']

# Example

string_1 = 'I quit smoking'
new_list_1 = list(string_1) # we created multi element list
print(new_list_1) # ['I', ' ', 'q', 'u', 'i', 't', ' ', 's', 'm', 'o', 'k', 'i', 'n', 'g']

new_list_2 = [string_1] # this is a single element list
print(new_list_2) # ['I quit smoking']

# Example
my_list = ['Ali', 'Tom', 2022]
new_l = list(my_list)
new_l2 = [my_list]

print(new_l) # ['Ali', 'Tom', 2022]
print(len(new_l)) # 3
print(new_l2) # [['Ali', 'Tom', 2022]]
print(len(new_l2)) # 1


