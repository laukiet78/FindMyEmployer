import hashlib, os
import logging
from extensions import mysql
import IInsertJobDetails
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql



class Databaselayer_InsertJob(IInsertJobDetails.IInsertJobDetails):
    def insertJob_DBL(Self,jobId,companyName,title,manager,location,jobDetails):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.callproc('spInsertJobDetails',[jobId,companyName,title,manager,location,jobDetails])
            conn.commit()
            msg = "Successfully Added"
        except:
            conn.rollback()
            excep_msg = "Error occured in insertJob_DBL method"
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return msg
