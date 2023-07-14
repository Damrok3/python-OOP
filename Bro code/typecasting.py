# type casting = converts the data type of a value to another data type

x = 1 # int
y = 2.0 #float
z = "3" #str

y = int(y)
z = str(z)
x = float(x)

L = [y,z,x]

for item in L:
    print(type(item))