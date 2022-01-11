# Searching a String

#We will use some methods to find out strings

# string.startswith()
# Starts searching from the beginning to the end. Gives Boolean result

# string.endswith()
# Starts seaching from the very end to the beginning. 
# Gives Boolean result

text = 'www.clarusway.com'
print(text.endswith('.com'))
print(text.startswith('http:'))

text = 'www.clarusway.com'
print(text.endswith('om'))
print(text.startswith('w'))

text = 'www.clarusway.com'
print(text.startswith('lc'))
print(text.endswith('ya'))

text = 'clarusway'
print(text.startswith('u',4))

print(text.startswith('w',6,7))