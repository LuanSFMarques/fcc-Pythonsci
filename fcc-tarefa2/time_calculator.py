def add_time(time,timesum,dayname=""):
    daycount = 0

    timesplit1 = time.split()
    timesplit2 = timesplit1[0].split(":")

    timesumsplit1 = timesum.split()
    timesumsplit2 = timesumsplit1[0].split(":")

    firstpart = (int(timesplit2[0])+(int(timesumsplit2[0])))

    secpart = (int(timesplit2[1])+(int(timesumsplit2[1])))

    if secpart>=60:
        secpart -= 60
        firstpart += 1

    #final verify
    if firstpart >= 12:
        fcopy = firstpart
        while fcopy >= 12:
            fcopy -= 12
            if timesplit1[1] == "PM":
                timesplit1[1] = "AM"
                daycount += 1
            elif timesplit1[1] == "AM":
                timesplit1[1] = "PM"
    if firstpart >= 13:
        while firstpart >= 13:
            firstpart -= 12
    days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    try:
        current_index = days_of_week.index(dayname.lower())
        new_index = (current_index + daycount) % 7
        new_dayname = days_of_week[new_index]
    except:
        dayname = ""

    final = str(firstpart)+":"+str("{:02d}".format(secpart))+ ' ' +timesplit1[1]
    if dayname != "":
        final += ", "+new_dayname.capitalize()
    if daycount == 0:
        return final
    elif daycount == 1: 
        return ((final)+ " (next day)")
    elif daycount > 1:    
        return ((final)+ " ("+str(daycount)+" days later)")