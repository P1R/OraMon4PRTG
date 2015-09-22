#    Copyright 2015 David Eugenio Perez Negron Rocha
#
#    This file is part of OraMon4PRTG.
#
#    OraMon4PRTG is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
#    OraMon4PRTG is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along with OraMon4PRTG. If not, see http://www.gnu.org/licenses/.
from OrMgr import OrMgr
class Checks(OrMgr):
    ''' Multiple Predefined Monitoring SQL Querys'''
    def ChkSize(self, TableName):
        '''Check Size in MB of a Table'''
        sql = "select segment_name,segment_type,bytes/1024/1024 MB \
                from dba_segments \
                where segment_type='TABLE' \
                and segment_name='{0}'".format(TableName)
        self.cur.execute(sql)
        for i in self.cur:
            return i[2]
    def ChkRows(self, TableName):
        "no funciona query verificar con que usuario se hace"
        #sql = "select {0}.num_rows, {0}.table_name from user_tables {0}".format(TableName)
        #sql = "select count({0}.num_rows) from user_tables {0}".format(TableName)
        sql = "select count(*) from user_tables {0}".format(TableName)
        self.cur.execute(sql)
        for i in self.cur:
            return i[0]
    def asm_volume_use(self, name):
        '''Display Percentage usage of an ASM Table'''
        sql = "select round(((TOTAL_MB-FREE_MB)/TOTAL_MB*100),2) from \
                v$asm_diskgroup_stat where name = '{0}'".format(name)
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            return i[0]
    def ChkTblSpace(self,TableName):
        '''Return Table space usage info, output Example:
        TABLESPACE                USED_MB    FREE_MB   TOTAL_MB   PCT_FREE
        ---------------------- ---------- ---------- ---------- ----------
        DCS_D_01                      263         31        294         11
		'''
        sql = "select df.tablespace_name tablespace,\
				totalusedspace used_mb,\
				(df.totalspace - tu.totalusedspace) free_mb,\
				df.totalspace total_mb,\
				round(100 * ( (df.totalspace - tu.totalusedspace)/ df.totalspace)) pct_free\
						from\
						(select tablespace_name,\
						round(sum(bytes) / 1048576) totalspace\
						from dba_data_files \
						group by tablespace_name) df,\
						(select round(sum(bytes)/(1024*1024)) totalusedspace, tablespace_name\
						from dba_segments \
						group by tablespace_name) tu\
						where df.tablespace_name = tu.tablespace_name \
						and df.tablespace_name = '{0}'".format(TableName)
        self.cur.execute(sql)
        res = self.cur.fetchall()
		#for return pct_free 
        for i in res:
            return (100-i[4])       

