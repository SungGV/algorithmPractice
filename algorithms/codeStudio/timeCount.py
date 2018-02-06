'''
You are given a huge log file which holds the entry and exit time of each person entering and exiting the office on a given day

format of file:
entry time exit time
09:12:23 11:14:35
10:34:01 13:23:40
10:34:31 11:20:10

upto N entries for a given day

Design a function which returns the total number of persons in the office at any given time. e.g input to function is 11:05:20.

The interviewer said he could call the function every second with input 11:05:20, 11:05:21,11:05:22, 11:05:23..........14:30:30
'''


from datetime import datetime


data = [
    ['09:12:23', '11:14:35'],
    ['10:34:01', '13:23:40'],
    ['10:34:31', '11:20:10']
]

def is_inOffice(time):
    format = "%H:%M:%S"
    cnt = 0
    for d1, d2 in data:
        if datetime.strptime(d1, format) <= datetime.strptime(time, format) < datetime.strptime(d2, format):
            cnt += 1

    print(cnt)
is_inOffice("11:05:20")
