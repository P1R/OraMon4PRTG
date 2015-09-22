#    Copyright 2015 David Eugenio Perez Negron Rocha
#
#    This file is part of OraMon4PRTG.
#
#    OraMon4PRTG is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
#    OraMon4PRTG is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along with OraMon4PRTG. If not, see http://www.gnu.org/licenses/.
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

