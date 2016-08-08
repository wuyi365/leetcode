from datetime import datetime

ss  = '2016-05-11T03:19:17.767Z'
dateFormat = '%Y-%m-%dT%H:%M:%S.%fZ'

print datetime.strptime(ss, dateFormat)
print datetime.strptime("2008-09-03T20:56:35.450686Z", "%Y-%m-%dT%H:%M:%S.%fZ")
