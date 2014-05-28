#coding:utf8
import MySQLdb
import sys
import os
import ConfigParser
import Unicode
import time
import datetime

reload(sys)
sys.setdefaultencoding("utf8")

#now = time.localtime()
#str_now = time.strftime("%Y%m%d%H%M%S", now )
#tmpDB = 'DB_TMP'+str_now

config = ConfigParser.ConfigParser()
config.readfp(open("conf/adm.conf"),"rb")

host = config.get("Global","host")
port = int(config.get("Global","port"))
user = config.get("Global","user")
passwd = config.get("Global","password")

class MysqlQuery():
        def __init__(self):
                pass;

        def query_select(self,sqlCommand):
                try:
                        conn = MySQLdb.connect(
                                host = host,
                                user = user,
                                port = port,
                                passwd = passwd
                        )
                        cur=conn.cursor()
                        cur.execute(sqlCommand)
                        ret = ''
                        ret = cur.fetchall()
                        return  list(ret)
                        cur.close()
                        conn.close()
                except Exception,ex:
                        print Exception,":",ex

        def query_update(self,sqlCommand):
                try:
                        conn = MySQLdb.connect(
                                host = host,
                                user = user,
                                port = port,
                                passwd = passwd
                        )
                        cur=conn.cursor()
                        cur.execute(sqlCommand)
                        conn.commit()
                        cur.close()
                        conn.close()
                except Exception,ex:
                        print Exception,":",ex
