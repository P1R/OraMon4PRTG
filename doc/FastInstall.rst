OraMon4PRTG Fast Install
========================
NOTE: **For doing this you must verify you're logged in as root user**

Create folder path into the system
----------------------------------
::

    # mkdir /var/prtg
    # mkdir /var/prtg/scriptsxml

Clone with git the program files
--------------------------------
::

    # cd /var/prtg/scriptsxml
    # git clone https://github.com/P1R/OraMon4PRTG.git

Give PRTG user permissions
--------------------------
::

    # chown -Rv user.group /var/prtg

where the **user** and **group** are for the monitor user you want to use.
::

    # chmod u+x /var/prtg/scriptsxml/OraMon4PRTG/Main.py

Edit config file
----------------
Edit the config.py file so that you can add at dictionary Database

* username for Oracle.
* password for Oracle.
* IP address where the Oracle DB is hosted.
* Oracle database name

for further information see The
:class:`config`
file

Add ssh script advance into prtg
--------------------------------

