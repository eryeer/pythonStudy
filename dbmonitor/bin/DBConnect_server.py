#!/usr/bin/python
# coding:utf-8
import pymysql
import sys
import configparser
import os

def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, relpath, name)
            return os.path.normpath(os.path.abspath(full_path))
conf_filepath = findfile('D://CloudStation//project//pandas','sysmonitor.cnf')

cf=configparser.ConfigParser()
#cf.read('D:\CloudStation\project\pandas\conf\ods.cnf')
cf.read(conf_filepath)
dbhost =cf.get("sys","db_host")
dbuser = cf.get("sys","db_user")
dbpass = cf.get("sys","db_pass")
dbport = cf.getint("sys","db_port")
dbdump=cf.get("sys","db_dump")

class DBConnect():
    def __init__(self):
        self.host=dbhost
        self.user=dbuser
        self.passwd=dbpass
        self.port=dbport
        self._conn=self.GetConnect()
        if (self._conn):
            self._cur=self._conn.cursor(pymysql.cursors.DictCursor)

    def GetConnect(self):
        conn=False
        try:
            conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, port=self.port,charset='utf8')
        except Exception as err:
            print("连接数据库失败，%s" %err)
        else:
            return conn

    def ExecQuery(self,sql):
        res = ''
        try:
            self._cur.execute(sql)
            self._conn.commit()
            res=self._cur.fetchall()
        except Exception as err:
                print("SQL执行失败,%s" % err)
        else:
            return res

    def CLose(self):
         if(self._conn):
             try:
                self._cur.close()
                self._conn.close()
             except:
                 raise("关闭异常,%s,%s" % (type(self._cur),type(self._cur)))
