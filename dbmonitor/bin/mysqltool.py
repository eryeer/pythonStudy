#!/usr/bin/python
# coding:utf-8
import pandas as pd
from texttable import Texttable
from DBConnect_server import DBConnect
import DBConnect_server

dumpfilepath=DBConnect_server.dbdump
class TOPSQL:
    def HOTSQL(self):
        try:
           dbconn = DBConnect()
           hotsql='select db,exec_count,query from sys.statement_analysis order by exec_count desc limit 10;'
           ds_hot=dbconn.ExecQuery(hotsql)
           pd.set_option('expand_frame_repr',False)
           # pd.set_option('date_dayfirst',True)
           self.df = pd.DataFrame(list(ds_hot))
           return self.df
        except Exception as err:
            print ('failed')
        finally:
            dbconn.CLose()

    def TOCSV(self):
        return self.df.to_csv(dumpfilepath + 'HOTSQL.csv',index=False)

class FILEIO:
    def MOSTIO(self):
        try:
           dbconn = DBConnect()
           hotsql='select * from sys.io_global_by_file_by_bytes limit 10;'
           ds_hot=dbconn.ExecQuery(hotsql)
           pd.set_option('expand_frame_repr',False)
           # pd.set_option('date_dayfirst',True)
           self.df = pd.DataFrame(list(ds_hot))
           return self.df
        except Exception as err:
            print ('failed')
        finally:
            dbconn.CLose()

    def TOCSV(self):
        self.df.to_csv(dumpfilepath + 'FILEIO.csv',index=False)

class TABLEIO:
    def MOSTTABLEIO(self):
        try:
           dbconn = DBConnect()
           hotsql="select * from sys.io_global_by_file_by_bytes where file like '%ibd' order by total desc limit 10;"
           ds_hot=dbconn.ExecQuery(hotsql)
           pd.set_option('expand_frame_repr',False)
           # pd.set_option('date_dayfirst',True)
           self.df = pd.DataFrame(list(ds_hot))
           return self.df
        except Exception as err:
            print ('failed')
        finally:
            dbconn.CLose()

    def TOCSV(self):
        self.df.to_csv(dumpfilepath + 'TABLEIO.csv',index=False)

class LATESQL():
    def TOPLATESQL(self):
        try:
            dbconn = DBConnect()
            hotsql = "select * from sys.statement_analysis order by avg_latency desc limit 10;"
            ds_hot = dbconn.ExecQuery(hotsql)
            pd.set_option('expand_frame_repr', False)
            # pd.set_option('date_dayfirst',True)
            self.df = pd.DataFrame(list(ds_hot))
            return self.df
        except Exception as err:
            print('failed')
        finally:
            dbconn.CLose()

    def TOCSV(self):
        self.df.to_csv(dumpfilepath + 'LATESQL.csv', index=False)

class TMPSQL():
    def TMPTABLESQL(self):
        try:
            dbconn = DBConnect()
            hotsql = " select db, query, tmp_tables, tmp_disk_tables  from sys.statement_analysis " \
                     "where tmp_tables>0 or tmp_disk_tables >0 order by (tmp_tables+tmp_disk_tables) desc limit 20;"
            ds_hot = dbconn.ExecQuery(hotsql)
            pd.set_option('expand_frame_repr', False)
            # pd.set_option('date_dayfirst',True)
            self.df = pd.DataFrame(list(ds_hot))
            return self.df
        except Exception as err:
            print('failed')
        finally:
            dbconn.CLose()

    def TOCSV(self):
        self.df.to_csv(dumpfilepath + 'TMPSQL.csv', index=False)

class CONN():
    def CONNECTPERMEM(self):
        try:
            dbconn = DBConnect()
            hotsql = " select b.user, current_count_used, current_allocated, current_avg_alloc, current_max_alloc, " \
                     "total_allocated,current_statement from sys.memory_by_thread_by_current_bytes a, session b where a.thread_id = b.thd_id;"
            ds_hot = dbconn.ExecQuery(hotsql)
            pd.set_option('expand_frame_repr', False)
            # pd.set_option('date_dayfirst',True)
            self.df = pd.DataFrame(list(ds_hot))
            return self.df
        except Exception as err:
            print('failed')
        finally:
            dbconn.CLose()

    def CONNFROM(self):
        try:
            dbconn = DBConnect()
            hotsql = " select host, current_connections, statements from host_summary; "
            ds_hot = dbconn.ExecQuery(hotsql)
            pd.set_option('expand_frame_repr', False)
            # pd.set_option('date_dayfirst',True)
            self.df = pd.DataFrame(list(ds_hot))
            return self.df
        except Exception as err:
            print('failed')
        finally:
            dbconn.CLose()

    def TOCSV(self):
        self.df.to_csv(dumpfilepath + 'CONNECTPERMEM.csv', index=False)

class INDX():
    def REDUNDANTINDX(self):
        try:
            dbconn = DBConnect()
            hotsql = " select * from sys.schema_redundant_indexes;"
            ds_hot = dbconn.ExecQuery(hotsql)
            pd.set_option('expand_frame_repr', False)
            # pd.set_option('date_dayfirst',True)
            self.df = pd.DataFrame(list(ds_hot))
            return self.df
        except Exception as err:
            print('failed')
        finally:
            dbconn.CLose()

    def UNUSEDINDEX(self):
        try:
            dbconn = DBConnect()
            hotsql = " select * from sys.schema_unused_indexes;"
            ds_hot = dbconn.ExecQuery(hotsql)
            pd.set_option('expand_frame_repr', False)
            # pd.set_option('date_dayfirst',True)
            self.df = pd.DataFrame(list(ds_hot))
            return self.df
        except Exception as err:
            print('failed')
        finally:
            dbconn.CLose()

    def TORICSV(self):
        self.df.to_csv(dumpfilepath + 'REDUNDANTINDEX.csv', index=False)

    def TOUICSV(self):
        self.df.to_csv(dumpfilepath + 'UNUSEDINDEX.csv', index=False)

class FULLSCAN():
    def FSSQL(self):
        try:
            dbconn = DBConnect()
            hotsql = " select * from sys.statements_with_full_table_scans; "
            ds_hot = dbconn.ExecQuery(hotsql)
            pd.set_option('expand_frame_repr', False)
            # pd.set_option('date_dayfirst',True)
            self.df = pd.DataFrame(list(ds_hot))
            return self.df
        except Exception as err:
            print('failed')
        finally:
            dbconn.CLose()

    def TOCSV(self):
        self.df.to_csv(dumpfilepath + 'FULLSCAN.csv', index=False)

class BUFFERTABLE():
    def MOSTBT(self):
        try:
            dbconn = DBConnect()
            hotsql = " select * from sys.innodb_buffer_stats_by_table order by allocated desc limit 10; "
            ds_hot = dbconn.ExecQuery(hotsql)
            pd.set_option('expand_frame_repr', False)
            # pd.set_option('date_dayfirst',True)
            self.df = pd.DataFrame(list(ds_hot))
            return self.df
        except Exception as err:
            print('failed')
        finally:
            dbconn.CLose()

    def TOCSV(self):
        self.df.to_csv(dumpfilepath + 'BUFFERTABLE.csv', index=False)

class AUTOINC():
    def MAXAUTOINC(self):
        try:
            auto_db=input("请输入数据库名：")
            auto_table=input("请输入数据表名：")
            dbconn = DBConnect()
            hotsql = " select * from sys.schema_auto_increment_columns where table_schema= '%s' and table_name = '%s'" %(auto_db,auto_table)
            ds_hot = dbconn.ExecQuery(hotsql)
            pd.set_option('expand_frame_repr', False)
            # pd.set_option('date_dayfirst',True)
            self.df = pd.DataFrame(list(ds_hot))
            return self.df
        except Exception as err:
            print('failed')
        finally:
            dbconn.CLose()

    def TOCSV(self):
        self.df.to_csv(dumpfilepath + 'AUTOINC.csv', index=False)

class UNCOMMIT():
    def UNCOMMSQL(self):
        try:
            dbconn = DBConnect()
            hotsql = "select a.sql_text,c.id,d.trx_started from performance_schema.events_statements_current a join performance_schema.threads b " \
                     "on a.thread_id=b.threade_id join information_schema.processlist c on b.processlist_id=c.id " \
                     "join information_schema.innodb_trx d on c.id=d.trx_mysql_thread_id order by d.trx_started;"
            ds_hot = dbconn.ExecQuery(hotsql)
            pd.set_option('expand_frame_repr', False)
            # pd.set_option('date_dayfirst',True)
            self.df = pd.DataFrame(list(ds_hot))
            return self.df
        except Exception as err:
            print('failed')
        finally:
            dbconn.CLose()

    def TOCSV(self):
        self.df.to_csv(dumpfilepath + 'UNCOMMIT.csv', index=False)

class WAITSQL():
    def LOCKWAITSQL(self):
        try:
            dbconn = DBConnect()
            hotsql = "select r.trx_mysql_thread_id waiting_thread,r.trx_query waiting_query,b.trx_mysql_thread_id blocking_thread," \
                     "b.trx_query blocking_query from information_schema.innodb_lock_waits w inner join information_schema.innodb_trx b " \
                     "on b.trx_id= w.blocking_trx_id inner join information_schema.innodb_trx r on r.trx_id=w.requesting_trx_id"
            ds_hot = dbconn.ExecQuery(hotsql)
            pd.set_option('expand_frame_repr', False)
            #去除中间省略号
            pd.set_option('display.width', None)
            #去除100行限制
            pd.set_option('display.max_rows', None)
            # pd.set_option('date_dayfirst',True)
            self.df = pd.DataFrame(list(ds_hot))
            return self.df
        except Exception as err:
            print('failed')
        finally:
            dbconn.CLose()

    def TOCSV(self):
        self.df.to_csv(dumpfilepath + 'WAITSQL.csv', index=False)

def textdraw(df):
    col_types=['t']
    col_align=['r']
    tb = Texttable(max_width=0)
    tdf = df
    number=len(tdf.columns.get_values())
    for i in range(number-1):
        col_types.append("t")
        col_align.append("r")
    tb.set_cols_align(col_align)
    tb.set_cols_dtype(col_types)
    tb.header(tdf.columns.get_values())
    tb.add_rows(tdf.values, header=False)
    return tb


class Main(object):
    def main(self):
        active = True
        while active:
            print("请选择功能，退出输入quit：")
            print("1.TOP10最热SQL语句")
            print("2.产生了最多IO的文件")
            print("3.产生了最多IO的表")
            print("4.延迟最多的SQL语句")
            print("5.使用了临时表的SQL语句")
            print("6.每个链接分配的内存")
            print("7.冗余的索引")
            print("8.未使用的索引")
            print("9.全表扫描的SQL语句")
            print("10.当前连接情况")
            print("11.占用最多buffer的表")
            print("12.自增长字段的最大值和当前已经使用到的值")
            print("13.未提交的SQL语句")
            print("14.锁等待SQL语句")
            monitfunction=input("请输入数字：")
            if (monitfunction == '1'):
                b=TOPSQL()
                df = b.HOTSQL()
                if (df.empty == True):
                    print ("没有SQL语句在执行")
                else:
                    tb=textdraw(df)
                    print(tb.draw())
                tocsv=input("是否要输出csv?(y/n)")
                if (tocsv.lower()=='y'):
                    b.TOCSV()
                iscontinue=input('是否要退出?(y/n)')
                if (iscontinue.lower()=='y'):
                    active=False
            if (monitfunction == '2'):
                b=FILEIO()
                df = b.MOSTIO()
                if (df.empty == True):
                    print ("没有SQL语句在执行")
                else:
                    tb=textdraw(df)
                    print (tb.draw())
                tocsv = input("是否要输出csv?(y/n)")
                if (tocsv.lower()=='y'):
                    b.TOCSV()
                iscontinue=input('是否要退出?(y/n)')
                if (iscontinue.lower()=='y'):
                    active=False
            if (monitfunction == '3'):
                b=TABLEIO()
                df=b.MOSTTABLEIO()
                if (df.empty ==True):
                    print ("表上没有IO")
                else:
                    tb=textdraw(df)
                    print (tb.draw())
                tocsv = input("是否要输出csv?(y/n)")
                if (tocsv.lower()=='y'):
                    b.TOCSV()
                iscontinue=input('是否要退出?(y/n)')
                if (iscontinue.lower()=='y'):
                    active=False
            if (monitfunction == '4'):
                b=LATESQL()
                df=b.TOPLATESQL()
                if (df.empty ==True):
                    print ("没有延迟的IO")
                else:
                    tb=textdraw(df)
                    print (tb.draw())
                tocsv = input("是否要输出csv?(y/n)")
                if (tocsv.lower()=='y'):
                    b.TOCSV()
                iscontinue=input('是否要退出?(y/n)')
                if (iscontinue.lower()=='y'):
                    active=False
            if (monitfunction == '5'):
                b=TMPSQL()
                df=b.TMPTABLESQL()
                if (df.empty ==True):
                    print ("没有使用零时表的SQL语句")
                else:
                    tb=textdraw(df)
                    print (tb.draw())
                tocsv = input("是否要输出csv?(y/n)")
                if (tocsv.lower()=='y'):
                    b.TOCSV()
                iscontinue=input('是否要退出?(y/n)')
                if (iscontinue.lower()=='y'):
                    active=False
            if (monitfunction == '6'):
                b=CONN()
                df=b.CONNECTPERMEM()
                if (df.empty ==True):
                    print ("数据库里没有连接")
                else:
                    tb=textdraw(df)
                    print (tb.draw())
                tocsv = input("是否要输出csv?(y/n)")
                if (tocsv.lower()=='y'):
                    b.TOCSV()
                iscontinue=input('是否要退出?(y/n)')
                if (iscontinue.lower()=='y'):
                    active=False
            if (monitfunction == '7'):
                b=INDX()
                df=b.REDUNDANTINDX()
                if (df.empty ==True):
                    print ("数据库中没有冗余索引")
                else:
                    tb=textdraw(df)
                    print(tb.draw())
                tocsv = input("是否要输出csv?(y/n)")
                if (tocsv.lower()=='y'):
                    b.TORICSV()
                iscontinue=input('是否要退出?(y/n)')
                if (iscontinue.lower()=='y'):
                    active=False
            if (monitfunction == '8'):
                b=INDX()
                df=b.UNUSEDINDEX()
                if (df.empty ==True):
                    print ("数据库中没有未使用的索引")
                else:
                    tb=textdraw(df)
                    print(tb.draw())
                tocsv = input("是否要输出csv?(y/n)")
                if (tocsv.lower()=='y'):
                    b.TOUICSV()
                iscontinue=input('是否要退出?(y/n)')
                if (iscontinue.lower()=='y'):
                    active=False
            if (monitfunction == '9'):
                b=FULLSCAN()
                df=b.FSSQL()
                if (df.empty ==True):
                    print ("没有全表扫描的SQL")
                else:
                    tb=textdraw(df)
                    print(tb.draw())
                tocsv = input("是否要输出csv?(y/n)")
                if (tocsv.lower()=='y'):
                    b.TOCSV()
                iscontinue=input('是否要退出?(y/n)')
                if (iscontinue.lower()=='y'):
                    active=False
            if (monitfunction == '10'):
                b = CONN()
                df = b.CONNFROM()
                if (df.empty == True):
                    print("数据库里没有连接")
                else:
                    tb = textdraw(df)
                    print(tb.draw())
                tocsv = input("是否要输出csv?(y/n)")
                if (tocsv.lower() == 'y'):
                    b.TOCSV()
                iscontinue = input('是否要退出?(y/n)')
                if (iscontinue.lower() == 'y'):
                    active = False
            if (monitfunction == '11'):
                b=BUFFERTABLE()
                df=b.MOSTBT()
                if (df.empty ==True):
                    print ("没有表使用到buffer")
                else:
                    tb=textdraw(df)
                    print(tb.draw())
                tocsv = input("是否要输出csv?(y/n)")
                if (tocsv.lower()=='y'):
                    b.TOCSV()
                iscontinue=input('是否要退出?(y/n)')
                if (iscontinue.lower()=='y'):
                    active=False
            if (monitfunction == '12'):
                b=AUTOINC()
                df=b.MAXAUTOINC()
                if (df.empty ==True):
                    print ("查询的表没有自增主键")
                else:
                    tb=textdraw(df)
                    print(tb.draw())
                tocsv = input("是否要输出csv?(y/n)")
                if (tocsv.lower()=='y'):
                    b.TOCSV()
                iscontinue=input('是否要退出?(y/n)')
                if (iscontinue.lower()=='y'):
                    active=False
            if (monitfunction == '13'):
                b=UNCOMMIT()
                df=b.UNCOMMSQL()
                if (df.empty ==True):
                    print ("没有未提交的SQL")
                else:
                    tb=textdraw(df)
                    print(tb.draw())
                tocsv = input("是否要输出csv?(y/n)")
                if (tocsv.lower()=='y'):
                    b.TOCSV()
                iscontinue=input('是否要退出?(y/n)')
                if (iscontinue.lower()=='y'):
                    active=False
            if (monitfunction == '14'):
                b=WAITSQL()
                df=b.LOCKWAITSQL()
                if (df.empty ==True):
                    print ("数据库中没有锁等待语句")
                else:
                    tb=textdraw(df)
                    print(tb.draw())
                tocsv = input("是否要输出csv?(y/n)")
                if (tocsv.lower()=='y'):
                    b.TOCSV()
                iscontinue=input('是否要退出?(y/n)')
                if (iscontinue.lower()=='y'):
                    active=False
            elif (monitfunction.lower()=='quit'):
                active=False


if __name__ == "__main__":
    main_obj=Main()
    main_obj.main()
    # b = FILEIO()
    # b.FILEIO()
