# copyfile() =  copies contents of a file
# copy() =      copyfile() + permission mode + destination can be a driectory
# copy2() =     copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile("files\\test.txt","files\\copyfiletest.txt")