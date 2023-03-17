import time
hour = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
second = int(time.strftime('%S'))
if (hour >0 and hour < 12):
    print("Good Morning!!!")
elif (hour >= 12 and hour <17):
    print("Good Afternoon!!!")
else:
    print("Good Evening!!!")
print("The time is {}:{}:{}".format(hour,minute,second))