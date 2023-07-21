text = "Have a nice day, see ya"

with open("files\\writeafiletest.txt","a") as file:     # a is for append, w is for write and override, there's also other options.
    file.write(text)

    