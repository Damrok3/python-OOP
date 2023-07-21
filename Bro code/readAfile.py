try:
    with open("files\\test.tx") as file:   # using with open() will automatically close a file for you
        print(file.read())                  # once you're done with it. However this will not handle any exceptions.
    print(file.closed)
except FileNotFoundError:
    print("That file was not found :<")

