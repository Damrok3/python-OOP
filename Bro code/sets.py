# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()

dinner_table = utensils.union(dishes)

for x in dinner_table:
    print(x, end = " ")

print()

print(utensils.difference(dishes))
print(utensils.intersection(dishes))

print("\n")