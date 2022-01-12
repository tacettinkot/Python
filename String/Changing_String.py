# Changing a String

# string.method(arguments)
# The summary of some common and the most important methods are as follows
# string.upper() => Makes all chracters uppercase in string
# string.lower() => Makes all characters lowercase in string
# string.swapcase => changes lower to upper upper to lower characters
# string.title() => Changes fir letter to upper rest will be lower
# string.replace(old,new,count) => replace the letters to new one if we dont add count it will turn all characters to new one

# NOTE: We can use multiple methods in one time
#    Ex) str.lower().replace()....
    
sentence = 'I live and work in Virginia'
print(sentence.upper())
print(sentence.lower())
print(sentence.swapcase())
print(sentence)
print(sentence.replace('i','*'))
print(sentence.replace('i','$',2))

# Let’s change the first letters of each words to uppercase of the following text 👇
text = 'the better the family, the better the society'
text = text.title()
print(text)

# In the text below, accidentally the number 0(zero) is used  instead of the letter ‘o’ (oh). 
# Fix them using .replace() method and change the value of the variable considering the
# new text and print the result.
text = 'S0d0me and G0m0re'
text = text.replace('0','o')
print(text)

