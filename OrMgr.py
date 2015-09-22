#!/usr/bin/env python2.7

import cx_Oracle
import sys
from config import DbData as DbData

class OrMgr(object):
    '''Handling the Oracle connections'''

    def __init__(self):
        self.Get = DbData.get
        self.ConnectionError ="<prtg><Error>1</Error><Text>DB CONNECTION ERROR\
                  :\n please check if config.py data is ok or db Oracle is up\
                  </Text></prtg>"

    def db_connect(self):
        '''Conect to the Oracle DB with Info from config.py'''
        try:
            self.db = cx_Oracle.connect('''{0}/{1}@{2}/{3}'''.format(\
                    self.Get('username'),self.Get('password'),
                    self.Get('address'),self.Get('database')))
        except cx_Oracle.DatabaseError:
            print self.ConnectionError
            sys.exit()			
        self.cur = self.db.cursor()

    def db_close(self):
        '''disconect cursor and database'''
        self.cur.close()
        self.db.close()

if __name__ == "__main__":
    pass
