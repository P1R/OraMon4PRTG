The OraMon4PRTG Reference
=========================

What is OraMon4PRTG?
--------------------

Is a set of scripts in Python to implement Oracle instances monitoring for the 
paessler’s PRTG system included as an advanced ssh script

Software requirements
---------------------

* Python 2.7.x
* cx_Oracle 5.2 
* Red Hat Enterprise Linux Server release 5.8 or above 
* Oracle 11gR2 or above

About the code (Technical)
--------------------------

The config File
~~~~~~~~~~~~~~~~

*The config file was designer so certain data into it can 
startup the configuration for making OraMon4PRTG work*

.. automodule:: config
.. class:: config
.. attribute:: DbData

*section for DB connection datausername,password,address,database*

.. attribute:: TableSpaces
  
*format for table spaces is [ChannelName,MaxWarning,MaxError]*

  
The OrMgr Library
~~~~~~~~~~~~~~~~~~

*The OrMgr Library Handles the connections to the Oracle
Database, it takes as parameters the data into the DbData at*
:class:`config`
*file which also imports the cx_Oracle Library, so it can do it's job.*

.. automodule:: OrMgr
   :members:
   :member-order: bysource

The Checks Library
~~~~~~~~~~~~~~~~~~~

*The Checks Library is a set of Oracle querys defined as methods,
its work is to provide the Querys to be called so that a DBA 
that has no knowledge on the code can easily help the developer
to make special monitoring querys.*

.. automodule:: Checks
   :members:
   :member-order: bysource

The XMLTags Library
~~~~~~~~~~~~~~~~~~~

*The XMLTags Library is a shorter implementation of the xml format
so you can build methods faster usage calling the Checks Library
and printing in the XMLs PRTG format needed to display channels
with the data, you can develop your own methods for satifying your
needs.*

.. automodule:: XMLTags
   :members:
   :member-order: bysource

The Main File
-------------

*OraMon4PRTG requiers a main program which will be executed by the
advance ssh script, so now we will show two examples of the usage
and development of this final script.*

Example: The functions caller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This may or not be the basic example of usage for the PRTG advance
script monitor,the main idea is to reduce the code with the
:class:`XMLTags`
library and make your own special type of querys so that they can satisfy
your needs for display data at the PRTG ssh advace script.
It is also possible to include your own Querys in the
:class:`Checks`
Library so you can monitor special issues into your Oracle Database.

Now here is the example:
::

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

As you can see we predefined this functions into the
:class:`XMLTags`
Library for satisfying our monitoring needs in the Oracle DB.

hope you can do the same with this code ;)

Example: The table Spaces monitor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The next example shows how with the TableSpaces from The 
:class:`config`
file we wrote a list tof tablesspaces which are configure in order
to be consulted and display them in the PRTG monitor as 
one channel per tablespace.

::

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

NOTE: **since this function TblSpacs is recursive we may need to start and finish with the <prtg></prtg> format.**
