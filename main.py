import datetime
from playsound import playsound


def get_time():
    time = input("Please enter the alarm time in the hh:mm format\n")
    time_list = time.split(':')
    return time_list


def alarming(time):
    while True:
        if int(time[0]) == datetime.datetime.now().hour and int(time[1]) == datetime.datetime.now().minute:
            print("Alarming..")
            playsound("ringtone-126505.mp3")
            break


alarming(get_time())
