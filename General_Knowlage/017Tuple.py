# tuple =   collection which is ordered and unchangeable
#                used to group together related data

student = ("Bro",21,"male")
menu = ("Meal", "Appertize", "Deserts")

print("Items of menu is " +str(menu.__len__()))
print(menu.index("Deserts"))
print(student.count("Bro"))
print(student.index("male"))

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here!")
