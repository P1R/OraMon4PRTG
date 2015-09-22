#!/usr/bin/env python2.7

from Checks import Checks
from XMLTags import XMLTags
from config import TableSpaces as TableSpaces
if __name__ == "__main__":
    X = XMLTags()
    x = X.getData
    ChCk=Checks()
    ChCk.db_connect()
    TSGet = TableSpaces.get
	
    print "<prtg>"

    for keys,values in TableSpaces.items(): 
        print X.TblSpcs(TSGet(keys),ChCk.ChkTblSpace(keys)),
    print "</prtg>"
    ChCk.db_close()

