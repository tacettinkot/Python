# Editing a String
# â¸ The formula syntax ð
# string.method(arguments)
# The summary of some common and the most important methods are as follows ð
# str.strip() ==> removes all spaces from both sides
# str.rstrip() => removes spaces from the right side
# str.lstrip() => removes spaces from the left side

canli_yayin = "        clarusway        "
print(canli_yayin.strip().__len__())
print(canli_yayin.__len__())

str = "clarusway"
str.strip('cy')
# NOTE: removes trailing 'c' or 'y' or 'cy' or 'yc' from both sides

str.lstrip("cl")

str.lstrip("ay")
# NOTE: removes trailing 'a' or 'y' or 'ay' or 'ya' from left side

# Task ð
# â¹ In the text below, accidentally there are additional letters.
# Remove the additional letters and make the all words uppercase.
#â¹ Except for the print() line, your code should consist of a single line.
text = 'tyou can learn almost everything in pre-classz'
text = text.strip("tz").upper()
print(text)

# Task ð
# â¹ In the text below, accidentally the number the word âweâ is
# wrong written. Remove the additional âeâ letter and print the correct text.
# â¹ You can also use indexing/slicing/methods of string.
text = 'In God wee Trust'
print(text[:9]+text[10:]) 
print(text.replace("ee",'e'))

