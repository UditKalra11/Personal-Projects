import pyttsx3
engine = pyttsx3.init()
import random
import time

a=list(range(1,91))

random.shuffle(a)
t=float(input("Please enter the time interval (in secs): "))
for i in a:
    b=str(i)
    engine.say(b)
    print(i)
    engine.runAndWait()
    time.sleep(t)