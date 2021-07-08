from datetime import datetime
from playsound import playsound

print("     Welcome to The Alarm Clock\nPlease enter the alarm time :")

x = input("Hour (12-hour) : ")
while int(x) not in range(13):
    x = input("Please enter valid hour (12-hour) : ")
if len(x) == 1:
    x = '0' + x

y = input("Minutes : ")
while int(y) not in range(60):
    y = input("Please enter valid minutes (0-60) : ")
if len(y) == 1:
    y = '0' + y

p = input("AM/PM : ")
p_range = ["am","pm","AM","PM","Am","Pm"]
while p not in p_range:
    p = input("Please enter valid time period (AM/PM) : ")
if p == 'am' or p == 'Am':
    p = "AM"
if p == 'pm' or p == 'Pm':
    p = "PM"

name = input("Alarm Name : ")
print("Alarm set for\n%s:%s %s" %(x, y, p))

while True :
    now = datetime.now()
    nstr = now.strftime('%I:%M %p')
    if x == nstr[0] + nstr[1]:
        if y == nstr[3] + nstr[4]:
            if p == nstr[6] + nstr[7]:
                print("\n%s"%(name))
                playsound("D:\Lucifer.mp3")
                break