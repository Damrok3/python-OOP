# thread    =   a flow of execution. Like a seperate order of instructions.
#               however each thread takes a turn running to achieve concurrency
#               GIL = (global interpreter lock),
#               allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading

import threading
import time

start = time.perf_counter()

def eat_breakfast():
    time.sleep(3)
    print("you ate breakfast")

def drink_coffee():
    time.sleep(4)
    print("you drank coffee")

def study():
    time.sleep(5)
    print("you finished studying")

x = threading.Thread(target= eat_breakfast,args=())
x.start()
y = threading.Thread(target= drink_coffee,args=())
y.start()
z = threading.Thread(target= study,args=())
z.start()

x.join()    # makes the main thread to wait around for the thread x to finish before it can move on to its construction set
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter() - start)

