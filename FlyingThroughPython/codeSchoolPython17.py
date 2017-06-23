schedule_file = open('schedule.txt', 'r')
for line in schedule_file:
    show,time = line.split(' - ')
    print(show, time)
    print(line)
schedule_file.close()
