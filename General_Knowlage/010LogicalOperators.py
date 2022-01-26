# Logical operators (and, or, not) = used to check if two or more conditional statements are true

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("the temperature is good today")
    print("go outside")
elif -10 < temp < 0 or 50 > temp > 30:
    print("the temperature is bad today: ")
    print("Stay inside")
elif not(-10 < temp < 0 or 50 > temp > 30):
    print("the temperature is extremely bad today: ")
    print("Stay inside")