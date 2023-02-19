import os
from time import sleep, time
import sys
import threading
from threading import Thread
from _thread import interrupt_main
from signal import signal
from signal import SIGINT
lst = []

def star(s):
    result = ""
    for i in range(len(s)):
        if (i % 3 == 2):
            result += "*"
        result += s[i]
    print(result)

s = "The eye is a region of mostly calm weather at the center of a tropical cyclone."

tm = time()
star(s)

pid = os.fork()
if pid > 0:
    #os.execl()
    print("Process ID:", os.getpid())
    print("Child's process ID:", pid)
    print(time() - tm)

else:
    #os.execl()
    print("Process ID:", os.getpid())
    print(time() - tm)