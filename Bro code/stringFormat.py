# str.format() =    optional method that gives users
#                   more control when displaying output

animal = "Cow"
item = "moon"

# print("The " + animal + " junped over the " + item)
# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {0}".format(animal, item)) # positional argument
# print("The {animal} jumped over the {item}".format(animal = "Cow", item = "moon"))

text = "The {} jumped over the {}"
print(text.format(animal, item))


name = "Bro"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:<10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))

number = 1000

print("The number pi is {:.3f}".format(number)) # displays 3 digits after decimal portion (rounds numbers) 
print("The number pi is {:,}".format(number))   # will add coma every thousand 
print("The number pi is {:b}".format(number))   # binary representation
print("The number pi is {:o}".format(number))   # octal representation
print("The number pi is {:X}".format(number))   # hexadecimal representation
print("The number pi is {:e}".format(number))   # scientific notation



