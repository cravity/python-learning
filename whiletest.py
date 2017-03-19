from time import sleep
import subprocess
i = 1

while True:
    #print "Number: %d" % i
    subprocess.call(["uname", "-a"])
    if i == 10:
        break
    else:
        i += 1
        sleep(1)
