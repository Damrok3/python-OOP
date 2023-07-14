# slicing =   create a substring by extracting elements from another string
#             indexing[] or slice()
#             [start:stop:step]

name = "Bro Code"

first_name = name[:3]
last_name = name[4:]
funky_name = name[::2]
reversed_name = name[::-1]

L = [first_name, last_name, funky_name, reversed_name]

for each in L:
    print(each)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4) # -4 is an negative index

print(website1[slice])
print(website2[slice])