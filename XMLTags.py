#!/usr/bin/env python2.7

class XMLTags(object):
    '''This class handles the XMLtaging for PRTG's Advance Script
    requirements'''
    
    #add tags at constructor
    def __init__(self):
        '''Add Dictionarry with XMLtag and position to append Data'''
        self.Codes={"Cha": ["<channel></channel>\n", 9],
            "Val": ["<value></value>\n", 7],
            "Unt": ["<unit></unit>\n", 6],
            "CsU": ["<customUnit></customUnit>\n", 12],
            "SpS": ["<speedsize></speedsize>\n", 11],
            "VoS": ["<volumesize></volumesize>\n", 12],
            "SpT": ["<speedtime></speedtime>\n", 11],
            "Mod": ["<mode></mode>\n", 6],
            "Flt": ["<float></float>\n", 7],
            "DcM": ["<decimalmode></decimalmode>\n", 13],
            "WAR": ["<warning></warning>\n", 9],
            "ShC": ["<showchart></showchart>\n", 11],
            "ShT": ["<showtable></showtable>\n", 11],
            "LME": ["<limitmaxerror></limitmaxerror>\n", 15],
            "LMW": ["<limitmaxwarning></limitmaxwarning>\n", 17],
            "LmW": ["<limitminwarning></limitminwarning>\n", 17],
            "LmE": ["<limitminerror></limitminerror>\n", 15],
            "LEM": ["<limiterrormsg></limiterrormsg>\n", 15],
            "LWM": ["<limitwarningmsg></limitwarningmsg>\n", 17],
            "LiM": ["<limitmode></limitmode>\n", 11],
            "VLu": ["<valuelookup></valuelookup>\n", 13],
            "TXT": ["<text></text>\n", 6],
            "ERR": ["<error></error>\n", 7],
            "PRT": ["<prtg>\n</prtg>", 7],
            "Res": ["<result>\n</result>\n", 9]}

    def getData(self, Opt, Val):
        '''
        this function reads an Option code (see self.Codes) and a
        Value so it can append to the dictionary  tags and  return
        as an XML code
        '''
        tag = self.Codes.get(Opt)
        try:
            #search in Codes return tag until number+append
            #value+return endtag
            return tag[0][:tag[1]] + Val + tag[0][tag[1]:]
        except TypeError:
            Tp = type(Val)
            #verify is a int or float and turn to string
            if (Tp == int or Tp == float):
                Val = str(Val)
                return self.getData(Opt, Val)
            else:
                print "Type Error: Must use either string, float or integer,"
                print " as Val parameter"

    def S3p(self, Cha, Unt, Val):
        ''' simple 3 parameters (channel, unit, value)'''
        x = self.getData("Res",
            self.getData("Cha", Cha) +
            self.getData("Unt", Unt) +
            self.getData("Val", Val))
        return x

    def ScU(self, Cha, CsU, Val):
        '''simple Custom Unit'''
        x = self.getData("Res",
            self.getData("Cha", Cha) +
            self.getData("Unt", "Custom") +
            self.getData("CsU", CsU) +
            self.getData("Val", Val))
        return x
    def SFP(self, Cha, Val):
        '''Simple Float Percent'''
        x = self.getData("Res",
            self.getData("Cha", Cha) +
            self.getData("Flt",1) +
            self.getData("Unt","Percent") +
            self.getData("Val",Val))
        return x
    def TblSpcs(self,TS,Val):
        '''TS = [ChanelName,MaxWarning,Maxerror],Value'''
        x = self.getData("Res",
            self.getData("Cha", TS[0]) +
            self.getData("LiM", 1) +
            self.getData("LMW", TS[1]) +
            self.getData("LWM", ("Reached LimitWarning at " +
            str(TS[1]) + "% on " + str(TS[0]) + " tablespace")) +
            self.getData("LME", TS[2]) +
            self.getData("LWM", ("Reached LimitError at " +
            str(TS[2]) + "% on " + str(TS[0]) + " tablespace")) +
            self.getData("Flt",1) +
            self.getData("Unt","Percent") +
            self.getData("Val",Val))
        return x
'''
    def Bool(self, Val):
        # verify if is TRUE send OK MSG else Error
        if (Val == 1):
            x = self.getData("TXT","wms database is active, ok!")
        else:
            x = (self.getData("TXT","WMS DATABASE IS DOWN :(") +
                self.getData("ERR",1))
        return x
'''
if __name__ == "__main__":
   pass
