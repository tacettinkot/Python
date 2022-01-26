# To get info from user we use input() function
name = input("What is your name?: ")
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))

print("Hello "+name)
print("You are "+str(age)+" years old")
print("You are "+str(height)+"cm tall")
# When we use input function and assing a variable. We need to be careful about type of the variable
# We cannot use different data type in the same function. if we need to use it we have to use type cast
