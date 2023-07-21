import os

mypath = "C:\\Users\\ckm76\\OneDrive\\Desktop\\projekty\\coding\\python\\free codecamp course\\codecamp\\docs.txt"

if os.path.exists(mypath):
    print("That location exists")
    mypath = mypath.replace("\\docs.txt","")
    if os.path.isfile(mypath):
        print("that is a file")
    elif os.path.isdir(mypath):
        print("That is a directory")
else:
    print("That location doesn't exist")