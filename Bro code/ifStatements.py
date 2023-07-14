# if statement = a block of code that will execute if it's condition is true

age = int(input("How old are you?: "))

if age == 100:
    print("you're century old")
elif age >= 18:
    print("\nyou're an adult")
elif age < 0:
    print("\nyou haven't been born yet")
else:
    print("\nyou're a kid")
