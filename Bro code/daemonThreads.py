# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon thread cannot normally be killed, stay alive until task is complete

#                 ex. background tasks, garbage collection, waiting for input, long running processes

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, " seconds")

x = threading.Thread(target=timer, daemon=True)
x.start()

# x.setDaemon(True) # function that can also change thread from a normal to daemon type, remember to use it before initializing the thread though
print(x.isDaemon()) # returns true if a thread is of a daemon type

answer = input("Do you wish to exit?")

