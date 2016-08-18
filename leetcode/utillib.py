from datetime import datetime
import calendar as cal
import time

def dateStr2DateObj(datestring ='', dateFormat = '%Y-%m-%d-%H-%M'):
    print '---->'
    print datestring
    print dateFormat
    return datetime.strptime(str(datestring), dateFormat)

def utc8DateStrToUtc(datestring ='',dateFormat = '%Y-%m-%d %H:%M'):
    """
    why?
    date was saved as utc in DB

    for easy understand, translate to UTC+8(china time zone)
    """
    dateObj = datetime.strptime(str(datestring), dateFormat)
    timestampTime = time.mktime(dateObj.timetuple())

    #
    #
    utcDateTime = datetime.fromtimestamp(timestampTime- 8*60*60)
    utcDateTimeHour = utcDateTime.strftime('%Y-%m-%d %H:00:00')
    
    return utcDateTimeHour

def dbCursor2JsonMinute(dataCursor, utcStartTimeHour,startMinute, utcEndTimeHour, endMinute, interval = 6):
    """
    after the db querying, get the dataCursor, these data  cursor contains cpu, memory or other information

    to be used in highcharts, we need to convert them to highcharts suported data, pair list

    dataCursor: the query result of the db, like dataCursor = db['cpu'].find()
    interval: default is 6 seconds, if you don't want to many data, can set to others, only support x % 6 = 0, as we only collect data every 6 seconds
    """
    cpuUser = list()
    i = 0
    for data in dataCursor:

        timestampHourStr = data['timestamp_hour']
        timestampHour = datetime.strptime(str(timestampHourStr), '%Y-%m-%d %H:%M:%S')
        utcTimeStamp = cal.timegm(datetime.timetuple(timestampHour))

        d = data['values']
        listKeyInt = []
        for key, value in d.items():
            listKeyInt.append(int(key))
        for minute in sorted(listKeyInt):

            if timestampHourStr == utcStartTimeHour and minute < startMinute:
                continue
            elif timestampHourStr == utcEndTimeHour and minute > endMinute:
                continue
            else:

                minDict = data['values'][str(minute)]
                listKeyIntSecond = []
                # key mustr be string in mongoDB, so transalte to int and then sort
                #
                for key, value in minDict.items():
                  listKeyIntSecond.append(int(key))
                for second in sorted(listKeyIntSecond): 

                    # highcharts use millisecond directly, so translate to millisecond
                    #
                    if second % interval == 0:
                        timestampSecond = (utcTimeStamp + 60 *  int(minute) + int(second))* 1000
                        cpuUser.append([timestampSecond, data['values'][str(minute)][str(second)]])
                        i += 1
                    
    return cpuUser


def dbCursor2Jason(dataCursor, interval = 6, pointCount = None):
    """
    after the db querying, get the dataCursor, these data  cursor contains cpu, memory or other information

    to be used in highcharts, we need to convert them to highcharts suported data, pair list

    dataCursor: the query result of the db, like dataCursor = db['cpu'].find()
    interval: default is 6 seconds, if you don't want to many data, can set to others, only support x % 6 = 0, as we only collect data every 6 seconds
    """
    cpuUser = list()
    i = 0
    for data in dataCursor:
        timestampHour = data['timestamp_hour']
        timestampHour = datetime.strptime(str(timestampHour), '%Y-%m-%d %H:%M:%S')
        utcTimeStamp = cal.timegm(datetime.timetuple(timestampHour))

        d = data['values']
        listKeyInt = []
        for key, value in d.items():
            listKeyInt.append(int(key))
        for minute in sorted(listKeyInt):

            minDict = data['values'][str(minute)]
            listKeyIntSecond = []
            # key mustr be string in mongoDB, so transalte to int and then sort
            #
            for key, value in minDict.items():
                listKeyIntSecond.append(int(key))
            for second in sorted(listKeyIntSecond): 

                # highcharts use millisecond directly, so translate to millisecond
                #
                if second % interval == 0:
                    timestampSecond = (utcTimeStamp + 60 *  int(minute) + int(second))* 1000
                    cpuUser.append([timestampSecond, data['values'][str(minute)][str(second)]])
                    i += 1
                    
    if pointCount is not None:
        return cpuUser[-pointCount:]
    else:
        return cpuUser


def autoInterval(startTime, endTime):
    """
    automatically ajust data records according to the start time and end time

    this will avoid getting too much data if endtime and start time is too long

    e.g. if endTime - startTime > 12 hours, no need to get data every 6 second

    the rule is:
    endTime - startTime <=3 hours: interval = 6 seconds   10 data point every minitue, totally less than 3*60*10 = 1800
    3 hours < endTime - startTime <=6 hours: interval = 12 seconds 5 data point every minitue, totally less than 6*60*5 = 1800
    6 hours < endTime - startTime <=12 hours: interval = 24 seconds 3 data point every minitue, totally less than 12*60*3 = 2160
    12 hours < endTime - startTime <=24 hours: interval = 36 seconds 2 data point every minitue, totally less than 24*60*2 = 2880
    endTime - startTime > 24 hours: interval = 60 seconds 1 data every minitue, 1 day 1*24*60*1 = 1440; 3 days 3*24*60*1 = 4320

    """
    elapsedTime = endTime - startTime
    elapsedDays = elapsedTime.days

    if elapsedDays < 0:
        # invalid, end time is less than start time
        # will not show any records
        return 6 
    else:
        if elapsedDays == 0:
            elapsedHours = elapsedTime.seconds / 3600
            if elapsedHours <=3:
                return 6
            elif elapsedHours <=6 and elapsedHours >3:
                return 12
            elif elapsedHours <=12 and elapsedHours >6:
                return 24
            elif elapsedHours <=24 and elapsedHours >12:
                return 36
        elif elapsedDays >= 1:
            return 60