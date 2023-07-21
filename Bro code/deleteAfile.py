import os
import shutil
path = "files\\folder"

try:
    #os.remove(path)
    #os.rmdir(path)
    shutil.rmtree(path) #!!! dangerous function, deletes a folder and all files inside
except FileNotFoundError:
    print("that file was not found")
except PermissionError:
    print("you don't have a permission to delete that")
except OSError:
    print("you cannot delete that using that function")
else:
    print(path+" was deleted")
