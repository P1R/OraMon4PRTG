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

    print x("PRT",
            X.ScU("Size of DLYTRN","MegaBytes",
                ChCk.ChkSize('DLYTRN')) +
            X.S3p("Count Rows of DLYTRN","Count",
                ChCk.ChkRows('DLYTRN')) +
            X.SFP("ASM DATA percent usage",
				ChCk.asm_volume_use('DATA')) +
			X.TblSpcs(TSGet('SYSTEM'),50))
    ChCk.db_close()
