# scope = The region that a variable is recognised
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of variable can be created

name = "Bro" # global scope (available inside & outside of function)

def display_name():
    name = "Code"   # local scope (available only inside this function)
    print(name)

#print(name)
display_name()