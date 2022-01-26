# set = collection which is unordered, unindexed. No duplicate values
# set creats by {} curly braces

utensils = {"fork", "spoon", "knife", "knife", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

for i in utensils:
    print(i, end=" ")
print()
for j in dishes:
    print(j, end=" ")
print()
utensils.add("napkin")
utensils.remove("fork")
# utensils.clear() # its removes all items in set
dishes.update(utensils)
dinner_table = utensils.union(dishes)

print("Difrencess: ")
print(dishes.difference(utensils))
print("Commons: ")
print(utensils.intersection(dishes))

for x in utensils:
    print(x)
