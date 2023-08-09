import time

print(time.ctime(0))    # convert a time expressed in seconds since epoch to a readable string
                        # epoch = when your computer thinks time began (reference point)

print(time.time())      # how much time passed since the epoch in seconds

print(time.ctime(time.time()))  # time() gives current time and ctime() converts it to readable format

time_object = time.localtime()
print(time_object)
local_time = time.strftime("%B-%d-%Y %H:%M:%S", time_object)
print(local_time)

time_string = "20 April, 2020"
time_object1 = time.strptime(time_string, "%d %B, %Y")
print(time.strftime("%d-%B-%Y",time_object1))

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, #daylight savings time)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, -1)
time_string = time.asctime(time_tuple) # takes time tuple and converts it to string
print(time_string)
