'''section for DB Connection info'''
DbData={'username': 'SYSTEM',
        'password': 'orat3$',
        'address': '127.0.0.1',
        'database': 'wms',
        }
'''format for table spaces is [ChannelName,MaxWarning,MaxError]'''
TableSpaces={'SYSTEM': ['SYSTEM', 90, 95],
             'GEN_D_01': ['GEN_D_01', 90, 95],
             'DCS_D_03': ['DCS_D_03', 90, 95],
             'DCS_X_03': ['DCS_X_03', 90, 95],
             'SYSAUX': ['SYSAUX', 90, 95],
             'GEN_D_02': ['GEN_D_02', 90, 95],
             'GEN_X_01': ['GEN_X_01', 90, 95],
             'DCS_X_01': ['DCS_X_01', 90, 95],
             'DCS_D_01': ['DCS_D_01', 90, 95],
             'GEN_X_02': ['GEN_X_02', 90, 95],
             'DCS_X_04': ['DCS_X_04', 90, 95],
             'DCS_D_04': ['DCS_D_04', 90, 95]
             }

#section for module configuration and addin
#Modules={
