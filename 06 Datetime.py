from datetime import datetime
from time import sleep
#/home/pi/abc/log.txt
log = open("log.txt", "a")
for i in range(5):
  now = str(datetime. now())
  log.write("\ncurrent time is " + now + "\n")
  print(now)
  sleep(1)
log.flush()
log.close()
