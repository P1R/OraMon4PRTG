'''
    Copyright 2015 David Eugenio Perez Negron Rocha

    This file is part of OraMon4PRTG.

    OraMon4PRTG is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

    OraMon4PRTG is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with OraMon4PRTG. If not, see http://www.gnu.org/licenses/.

'''
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

