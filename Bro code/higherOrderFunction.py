# Higher Order Function = a function that either:
#                         1. accepts a function as an argument
#                               or
#                         2. returns a function
#                         (In python, functions are also treated as objects)

# vvvvvvvvvvvvv     accepts the function
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)

# vvvvvvvvvvvvv     returns a function
def divisor(x):
    def divident(y):
        return y / x
    return divident

# what happens is that first we're passing 2 and assigning it to X
# next we're skipping the divident function because we're not calling it there yet
# the divisor function returns the divident function with X being already inside of it and assigns it to divide variable
# inside of print, we're calling the divident function that sits inside of that variable and has x already inside of it, passing y into it as well
# then rest of the divident function gets exacuted 

divide = divisor(2)
print(divide(10))