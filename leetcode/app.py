#coding:utf-8
import calendar as cal
#import ConfigParser
from datetime import datetime
import time

from flask import Flask,render_template, request,json
from flask.ext.pymongo import PyMongo
from flask_restful import reqparse, abort, Api, Resource

from common import serverHost, servePort, db
from resources.DBStatistic import *
from resources.HardwareInfor import *
from resources.EnvInfo import *
from resources.SystemMonitorData import *

from util.utillib import *


app = Flask('cpu')
api = Api(app)

@app.route("/")
def indexest():
    return "Hello World!"

@app.route('/now')
def showNowUsage():
    machineList = db['cpu'].distinct( "server" )
    machineList.sort()
    return render_template('now.html', machineList= machineList)

@app.route('/cpu')
def showUsage():
    machineList = db['cpu'].distinct( "server" )
    machineList.sort()
    return render_template('cpu.html', machineList= machineList)


@app.route('/awr')
def createAwr():
    machineList = db['cpu'].distinct( "server" )
    machineList.sort()
    return render_template('awr.html', machineList= machineList)


def latestOneData():
    """
    real time monitoring, only get the latest one data.
    """

@app.route('/getCurrentData/<int:dataNumber>', methods=['POST'])
def getCurrentData(dataNumber):
    machineNames = request.form['machineName']
    

    # EndTime = datetime.strptime(str(EndTime), '%Y-%m-%d %H:%M')
    utcStartTimeHour  = datetime.utcnow().strftime('%Y-%m-%d %H:00:00')
    
    cpuSeriesData = []
    memorySeriesData = []
    networkioSentSeriesData = []
    networkioRecvSeriesData = []
    # people might input with blank, ignore blanks
    #
    for machineName in [x.strip() for x in machineNames.split(',') if x]:
        cpuUser = list()
        memUser = list()
        
        dataCursorCpu = db['cpu'].find({'server': machineName.upper(),'timestamp_hour':{'$gte': utcStartTimeHour}},{'timestamp_hour':1,'values':1, '_id':0}).limit(2)
        dataCursorMemory = db['memory'].find({'server': machineName.upper(),'timestamp_hour':{'$gte': utcStartTimeHour}},{'timestamp_hour':1,'values':1, '_id':0}).limit(2)
        

        cpuUser = dbCursor2Jason(dataCursorCpu, 6, dataNumber)
        memUser = dbCursor2Jason(dataCursorMemory, 6, dataNumber)
        # newworkIOsent = dbCursor2Jason(networkIOSent, intervalSeconds)
        # newworkIORecv = dbCursor2Jason(networkIORecv, intervalSeconds)

        #print '*****************querying cpu reuslt get count is*****************  ' + str(len(cpuUser))
        #print '*****************querying memory reuslt get count is*****************  ' + str(len(cpuUser))
        if len(cpuUser) > 0:
            cpuSeriesData.append({'name':machineName, 'data':cpuUser})
        if len(memUser) > 0:
            memorySeriesData.append({'name':machineName, 'data':memUser})
        #networkioSentSeriesData.append({'name':machineName, 'data':newworkIOsent})
       # networkioRecvSeriesData.append({'name':machineName, 'data':newworkIORecv})

   
    return json.dumps({
            # 'cpuUser': {'name':machineName, 'data':cpuUser},
            # 'memUser': memUser,
            'cpuUser': cpuSeriesData,
            'memUser': memorySeriesData,
           # 'newworkIOSent': networkioSentSeriesData,
            #'newworkIORecv': networkioRecvSeriesData,
         
            })



@app.route('/getData', methods=['POST'])
def getLoadData():
    machineNames = request.form['machineName']
    StartTime = request.form['StartTime']
    EndTime = request.form['EndTime']
    # checkedMachines = request.form['chkveg']


    # Usually use UTC+8 time, so translate to UTC time
    # as in DB, to be consistent with different timezone server machine, records data in DB are in UTC time
    #
    StartTime = datetime.strptime(str(StartTime), '%Y-%m-%d %H:%M')
    timestampStartTime = time.mktime(StartTime.timetuple())

    EndTime = datetime.strptime(str(EndTime), '%Y-%m-%d %H:%M')
    timestampEndTime = time.mktime(EndTime.timetuple())
    timestampEndTimeUTC =  (timestampEndTime - 8*60*60)*1000


    utcStartTime = datetime.fromtimestamp(timestampStartTime- 8*60*60)
    utcStartTimeHour = utcStartTime.strftime('%Y-%m-%d %H:00:00')
    utcStartTimeMinute = utcStartTime.minute


    utcEndTime = datetime.fromtimestamp(timestampEndTime- 8*60*60)
    utcEndTimeHour = utcEndTime.strftime('%Y-%m-%d %H:00:00')
    utcEndTimeMinute = utcEndTime.minute

    # EndTime = datetime.strptime(str(EndTime), '%Y-%m-%d %H:%M')
    intervalSeconds = autoInterval(StartTime, EndTime)
    
    cpuSeriesData = []
    memorySeriesData = []
    networkioSentSeriesData = []
    networkioRecvSeriesData = []
    # people might input with blank, ignore blanks
    #
    for machineName in [x.strip() for x in machineNames.split(',') if x]:
        cpuUser = list()
        memUser = list()
   
        dataCursorCpu = db['cpu'].find({'server': machineName.upper(),'timestamp_hour':{'$gte': utcStartTimeHour, '$lt': utcEndTimeHour}
           #  'values':{'$elemMatch' :{'$gte': utcStartTimeMinute, '$lt': utcEndTimeMinute}},
           },
            {'timestamp_hour':1,'values':1, '_id':0}).sort('timestamp_hour', 1)
        dataCursorMemory = db['memory'].find({'server': machineName.upper(),'timestamp_hour':{'$gte': utcStartTimeHour, '$lt': utcEndTimeHour}},
            {'timestamp_hour':1,'values':1, '_id':0}).sort('timestamp_hour', 1)

        networkIOSent = db['networkio'].find({'server': machineName.upper(),'type':'networkIOsent','timestamp_hour':{'$gte': utcStartTimeHour, '$lt': utcEndTimeHour}},
            {'timestamp_hour':1,'values':1, '_id':0}).sort('timestamp_hour', 1)
        networkIORecv = db['networkio'].find({'server': machineName.upper(),'type':'networkIOsent','timestamp_hour':{'$gte': utcStartTimeHour, '$lt': utcEndTimeHour}},
            {'timestamp_hour':1,'values':1, '_id':0}).sort('timestamp_hour', 1)
       # dataCursor = db['sf1-wpszprf304'].find({'date': {'$gte': int(1451293200000), '$lt': int(1451311200000)}})
        #print 'The db cpu query count is:    ' + str(dataCursorCpu.count())
        #print 'The db memory query count is:    ' + str(dataCursorMemory.count())
        cpuUser = dbCursor2Jason(dataCursorCpu, intervalSeconds)
        memUser = dbCursor2Jason(dataCursorMemory, intervalSeconds)
        newworkIOsent = dbCursor2Jason(networkIOSent, intervalSeconds)
        newworkIORecv = dbCursor2Jason(networkIORecv, intervalSeconds)

        #print '*****************querying cpu reuslt get count is*****************  ' + str(len(cpuUser))
        #print '*****************querying memory reuslt get count is*****************  ' + str(len(cpuUser))

        cpuSeriesData.append({'name':machineName, 'data':cpuUser})
        memorySeriesData.append({'name':machineName, 'data':memUser})
        networkioSentSeriesData.append({'name':machineName, 'data':newworkIOsent})
        networkioRecvSeriesData.append({'name':machineName, 'data':newworkIORecv})

   
    return json.dumps({
            # 'cpuUser': {'name':machineName, 'data':cpuUser},
            # 'memUser': memUser,
            'cpuUser': cpuSeriesData,
            'memUser': memorySeriesData,
            'newworkIOSent': networkioSentSeriesData,
            'newworkIORecv': networkioRecvSeriesData,
         
            })



@app.route('/getTrendData', methods=['POST'])
def getTrendData():

    # people might input with blank, ignore blanks
    #
    if 1:
        responsTime = []
        dataCursor = db['pt_response_time'].find({}).sort('testDate', 1)
        percent80 = list()
        percent90 = list()
        percent95 = list()
        for doc in dataCursor:
            testDate =  doc['testDate']
            
            timestamp = time.mktime(testDate.timetuple()) * 1000
            #timestamp = cal.timegm(testDate)
            percent80.append([timestamp,doc['responseTime']['percent80']])
            percent90.append([timestamp,doc['responseTime']['percent90']])
            percent95.append([timestamp,doc['responseTime']['percent95']])
           #  'values':{'$elemMatch' :{'$gte': utcStartTimeMinute, '$lt': utcEndTimeMinute}},
       # dataCursor = db['sf1-wpszprf304'].find({'date': {'$gte': int(1451293200000), '$lt': int(1451311200000)}})
        #print 'The db cpu query count is:    ' + str(dataCursorCpu.count())
   

        responsTime.append({'name':'80%', 'data':percent80})
        responsTime.append({'name':'90%', 'data':percent90})
        responsTime.append({'name':'95%', 'data':percent95})
     

   
    return json.dumps({
            # 'cpuUser': {'name':machineName, 'data':cpuUser},
            # 'memUser': memUser,
            'responseTime': responsTime,
            
         
            })
# api.add_resource(TodoList, '/todos')
# api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(HardwareInfor, '/basic/hardware')
api.add_resource(DBStatistic, '/db')
api.add_resource(DBTriggerStatistic, '/db/trigger')
api.add_resource(DBQueryStatistic, '/db/query')
api.add_resource(MahinesList, '/basic/mahineslist')

api.add_resource(EnvInfos, '/basic/envs')
api.add_resource(EnvInfo, '/basic/env/<string:id>')

api.add_resource(SystemMonitorData, '/monitor/server')

if __name__ == "__main__":
    
    app.run(host=serverHost,port = servePort, debug = True)