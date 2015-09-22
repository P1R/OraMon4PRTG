'''
    Copyright 2015 David Eugenio Perez Negron Rocha

    This file is part of OraMon4PRTG.

    OraMon4PRTG is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

    OraMon4PRTG is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with OraMon4PRTG. If not, see http://www.gnu.org/licenses/.

'''
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

