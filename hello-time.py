import time
import datetime

while True:
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print ("Current time = ", current_time)
    time.sleep(5)


