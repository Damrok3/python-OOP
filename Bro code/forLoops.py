# for loop = a statement that will execute it's block of code
#            a limited amount of times


#            while loop = unlimited
#            for loop = limited

import time

for i in range(10):
    print(i+1)

print("/////////////////////")

for i in range(50, 100+1,2):
    print(i)

print("/////////////////////")

for i in "Bro Code":
    print(i)

print("/////////////////////")

for seconds in range(10, -1, -1):
    print(seconds)
    time.sleep(1)
print("happy new year")