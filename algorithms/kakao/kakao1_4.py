import datetime

capacity = 2
bus_num = 2
time = 1

first_departing_time = 9

bus_schedule = []


given_data = ["08:00", "08:01", "08:02", "08:03", '08:04']
# given_data = ['09:10', '09:09', '08:00']
# given_data = ['09:00', '09:00', '09:00', '09:00']
# given_data = ['00:01', '00:01', '00:01', '00:01', '00:01']
# given_data = ['23:59']
# given_data = ['23:59'] * 16
# given_data = ["08:00",  "09:00", "09:00", "09:00","09:03", "09:05","09:06","09:07","09:09","09:09","09:10","09:11"]

timetable = [datetime.datetime.strptime(i, '%H:%M').time() for i in given_data]


def bus_schedule_creator():
    temp_min  = 0
    temp_hour = first_departing_time

    for _ in range(bus_num):
        if temp_min % 60 == 0 and temp_min != 0:
            temp_min = 0
            temp_hour += 1

        bus_schedule.append(datetime.time(temp_hour, temp_min))
        temp_min += time


bus_schedule_creator()

bus_schedule.sort()
timetable.sort()

def compute_line_in_time():
    if bus_schedule[-1] < timetable[0]:
        return bus_schedule[-1]

    on_board = 0
    index = 0
    on_board_last_index = 0

    for bus_dep_index, bus_depart_time in enumerate(bus_schedule):
        for k in range(index, len(timetable)):   # loop to compare on_board to capacity
            if timetable[k] <= bus_depart_time and on_board < capacity:
                on_board_last_index = k
                on_board += 1
                index = k+1
            else:
                break
        if bus_dep_index != len(bus_schedule) - 1:  # 맨 마지막 버스때는 on_board 값을 그대로 넘겨준다
            on_board = 0

    if on_board < capacity:
        return bus_schedule[-1]
    else:
        print('빼기 1')
        return timetable[on_board_last_index]


print(compute_line_in_time())









