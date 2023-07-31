import time
time_object = time.localtime()

local_time = time.strftime("%B, %Y, %H:%M:%S", time_object)
print(local_time)  