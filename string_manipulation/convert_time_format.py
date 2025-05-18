# Convert Time Format
# split the hour and minute
# take the hour and calculate modulo with 12 then save to hour variable
# that modulo result is 12 hour format hour
# check the splited hour greater than 12. is there show a.m else p.m
# join together and return to it.

def convertTimeFormat(hourtime):
    splitedHourAndTime = hourtime.split(":")
    joinVal = ",".join(splitedHourAndTime)
    splitHour = joinVal.split(",")
    hour = int(splitHour[0])%12
    meridiem = 'a.m'
    if int(splitedHourAndTime[0]) >= 12:
        meridiem = 'p.m'
    
    res = str(hour)+":"+splitedHourAndTime[1]+" "+meridiem
    return res
    
print(convertTimeFormat("13:45"))
print(convertTimeFormat("23:59"))
# mytime = 13:45
# print(mytime%12)