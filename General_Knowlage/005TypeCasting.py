# Type casting = convert the data type of a value to another data type

x = 1 # int
y = 2.0 # float
z = "3" # str

print(x)
print(y)
print(z*3)

y = int(y)
z = int(z)
x = float(x)

print(x)
print(y)
print(z)

# Why we use type cating is to concanate the string and number we get error to solve issue is type casting
print("X is " + str(x))
print("Y is " + str(y))