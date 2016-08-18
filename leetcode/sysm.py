from __future__ import print_function, unicode_literals
from datetime import datetime
import psutil
import pymongo
from pymongo import MongoClient
from pymongo.errors import AutoReconnect
import socket, time
import calendar as cal
import ConfigParser, os, inspect
import random

import pythoncom
import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import logging
import threading
inspect



logging.basicConfig(
    filename = 'monitorService.log',
    level = logging.DEBUG, 
    format = '[SysMonitor-service] %(levelname)-7.7s %(message)s'
)


# configParser = ConfigParser.RawConfigParser()
# currentFile = inspect.getfile(inspect.currentframe())
# configFilePath = os.path.dirname(os.path.dirname(currentFile))

# with open(os.path.join(configFilePath, 'config.ini'),'r') as configfile: 
#     configParser.readfp(configfile)

# dbHost = configParser.get('DBServer', 'DBServerName')
# dbPort = configParser.getint('DBServer', 'port')
dbHost = 'apc-wgroapp301'
dbPort = 27017

def connectRetryDB(retries = 10, gaptime = 300):
    """
    This service is auto-started after machine reboot
    Then there is a bug: if the db service is not started, then connect db will fail, we need to restart this monitor servie

    resolve method:
    check db connect first, if it's ok, go on 
    if db connect is failed or not active, retry to connect db before collecting monitor data

    """
    tyies = 0
    global db
    while tyies < retries:
        try:
            client = MongoClient(dbHost, dbPort)
            db_status = client.server_info()
            db = client.sysmonitor
            logging.info(type(db_status))
            if db_status['ok'] > 0:
                return True
        except AutoReconnect as e:
            logging.info('except for auto reconnect...')
            logging.info(e)
            tyies += 1
            logging.info('retrying mongo DB connection...trying times...')
            logging.info(tyies)
            time.sleep(gaptime)
        except pymongo.errors.ServerSelectionTimeoutError as err:
            logging.info('except for auto reconnect...')
            logging.info(err)
            time.sleep(gaptime)
    return False


timeTick = 6  # why 6?

# to be refined
# 1. db table re-design: MongdoDB Document-Oriented Design
# 2. connect to db and insert data per minute, this will low down IO and DB trafic. no need to update db every time, it's bad
#


def getUtcNowHour():
    return datetime.utcnow().strftime('%Y-%m-%d %H:00:00')

def getInfoDoc(hostName, UtcNowHour, infoType):
    """
    This is definition of dict/json data, which will be stroed into mongoDB.

    return: dict
    """
    infoDoc = dict()

    infoDoc['server'] = hostName
    infoDoc['timestamp_hour'] = UtcNowHour
    infoDoc['type'] = infoType
    infoDoc['num_samples'] = 0
    infoDoc['total_samples'] = 0
    infoDoc['values'] = {}

    return infoDoc

def continueGetInfor():
    logging.info("Calling method continueGetInfor, this will call gefInfor in a while loop....")
    while True:
        logging.info("in continueGetInfor loop, below is calling get Infor")
        gefInfor()

def gefInfor():
    """
    Get the system resource inforation, save to mongoDB.

    """ 
    logging.info("Monitoring system resoruce, please don't kill it....")
    time.sleep(random.random())  #what's this? trying to fix a bug...

    memoryDoc = dict()
    diskDoc = dict()
    hostName = socket.gethostname()
    
    #
    # your server might be in different timezone, to be consistent, save UTC timstatmp
    #
    utc_now = datetime.utcnow()
    UtcNowHour = datetime.utcnow().strftime('%Y-%m-%d %H:00:00')
    logging.info("Currently UTC now hour is: " + str(UtcNowHour))

    cpuDoc = getInfoDoc(hostName, UtcNowHour, 'cpu_used')
    memoryDoc = getInfoDoc(hostName, UtcNowHour, 'memory_used')
    networkIOsentDoc = getInfoDoc(hostName, UtcNowHour, 'networkIOsent')
    newworkIOrecvedDoc = getInfoDoc(hostName, UtcNowHour, 'networkIOrecv')

    db['cpu'].update({'timestamp_hour': UtcNowHour, 'server':hostName}, {'$setOnInsert':cpuDoc }, upsert = True)
    db['memory'].update({'timestamp_hour': UtcNowHour, 'server':hostName}, {'$setOnInsert':memoryDoc}, upsert = True)

    db['networkio'].update({'timestamp_hour': UtcNowHour, 'server':hostName, 'type': 'networkIOsent'}, {'$setOnInsert':networkIOsentDoc}, upsert = True)
    db['networkio'].update({'timestamp_hour': UtcNowHour, 'server':hostName, 'type': 'networkIOrecv'}, {'$setOnInsert':newworkIOrecvedDoc}, upsert = True)
    while(1):
        minute = datetime.utcnow().minute
        second = datetime.utcnow().second

        networkIOsentBefore = psutil.net_io_counters().bytes_sent
        networkIOrecvBefore = psutil.net_io_counters().bytes_recv

        time.sleep(1)
        networkIOsentAfter = psutil.net_io_counters().bytes_sent
        networkIOrecvAfter = psutil.net_io_counters().bytes_recv

        if (second % timeTick) == 0:
            cpuUsage = psutil.cpu_percent()
            memoryUsage = psutil.virtual_memory().percent

            networkIOsent = round((networkIOsentAfter - networkIOsentBefore) / 1024.0, 2)
            networkIOrecv = round((networkIOrecvAfter - networkIOrecvBefore) / 1024.0, 2)
       
            db['cpu'].update({'timestamp_hour': UtcNowHour, 'server':hostName},
                             {
                             '$set':{'values.'+str(minute) + '.'+str(second): cpuUsage},
                             '$inc':{'num_samples': 1, 'total_samples': cpuUsage }
                             }
                             )
            db['memory'].update({'timestamp_hour': UtcNowHour, 'server':hostName},
                             {
                             '$set':{'values.'+str(minute) + '.'+str(second): memoryUsage},
                             '$inc':{'num_samples': 1, 'total_samples': memoryUsage }
                             }
                             )
            db['networkio'].update({'timestamp_hour': UtcNowHour, 'server':hostName, 'type': 'networkIOsent'},
                             {
                             '$set':{'values.'+str(minute) + '.'+str(second): networkIOsent},
                             '$inc':{'num_samples': 1, 'total_samples': networkIOsent }
                             }
                             )
            db['networkio'].update({'timestamp_hour': UtcNowHour, 'server':hostName, 'type': 'networkIOrecv'},
                             {
                             '$set':{'values.'+str(minute) + '.'+str(second): networkIOrecv},
                             '$inc':{'num_samples': 1, 'total_samples': networkIOrecv }
                             }
                             )
        if minute == 59  and second == 59:
            logging.info("breaking one hour data, will be in next loop hour... now utc hour is %s, minite is %d, second is %d" %(UtcNowHour, minute, second))
            break
    
        
class AppServerSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "SystemMonitor"
    _svc_display_name_ = "Monitor system resource"
    _svc_description_ = "A python program to monitor system resource, e.g cpu, memory..."

    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)
        socket.setdefaulttimeout(60)
        self.stop_requested = False

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.stop_requested = True

    def SvcDoRun(self):
        # servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
        #                       servicemanager.PYS_SERVICE_STARTED,
        #                       (self._svc_name_,''))
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        #win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)
        self.main()

    def main(self):
        logging.info('Begins the main method...')
        dbconnected = connectRetryDB()
        if dbconnected:
            logging.info('DB connected...')

            runOnce = 0
            while(1):
                #gefInfor()
            
                    # why need a thread?
                # To fix a bug: couldn't stop the windows service:
                # the while loop need to monitor the win32 action, or else will timeout,
                    # so put the real method gefInfor() in a thread, as this method will always running to get system infor,
                # this will not response to win32 event within 
                #
                #
                if runOnce == 0:
                    t = threading.Thread(target=continueGetInfor, args = ())
                    t.daemon = True
                    t.start()
                    t.is_alive()
                    logging.info('Running in a threading...')
                    runOnce = 1
            
                if win32event.WaitForSingleObject(self.hWaitStop, 5000) == win32event.WAIT_OBJECT_0:
                    logging.info('Service stop requested, will break the loop for getting sys infor...')

                    break

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(AppServerSvc)
