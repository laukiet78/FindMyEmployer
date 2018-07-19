import logging
import sys
import os
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
import datetime


class LogggingExceptions_Database:
    def getlevelname(self,x):
        return {
             50: 'CRITICAL',
             40: 'ERROR',
             30: 'WARNING',
             20: 'INFO',
             10: 'DEBUG',
              0: 'NOTSET'
        }.get(x, 10)

    def loadMyExceptionInDb(self,logLevel,customMsg,logMsg):
        try:
            msg=""
            conn = mysql.connect()
            loglevelname = self.getlevelname(logLevel)
            cur = conn.cursor()
            userEmailId = "rohit.gs28@gmail.com"
            currenttime = datetime.datetime.now()
            currenttime = str(currenttime)
            logMsg = str(logMsg)
            print currenttime
            print logLevel
            print customMsg
            print logMsg
            print userEmailId
            print loglevelname
            cur.callproc('spInserErrorLogInDB',[logLevel,loglevelname,customMsg,logMsg,currenttime,userEmailId])
            conn.commit()
        except Exception as e:
            conn.rollback()
            excep_msg = "CRITICAL DB ERROR! Logging to database not possible!"
            print excep_msg
            logging.warning(excep_msg, exc_info=True)
        conn.close()
