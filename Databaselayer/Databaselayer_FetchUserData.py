import hashlib, os
import logging
from extensions import mysql
import IFetchProfileDetails
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror


class Databaselayer_FetchUserData(IFetchProfileDetails.IFetchProfileDetails):
    def getProfileData_DBL(Self,email):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.callproc('spGetCompleteUserDetails',[email])
            profileData = cur.fetchone()
        except Exception as e:
            conn.rollback()
            excep_msg = "Error occured in getProfileData_DBL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return profileData
