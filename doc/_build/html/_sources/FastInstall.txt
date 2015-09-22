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
There is quiet lots of tutorials how to add this, but as fast to remember
you must add the ssh with permissions for execution of the Main script as
ssh login user and password, PRTG automatically will verify this and you
also must select the script to use in our example it might be the **Main.py**

however there is always a documentation about this by the PRTG developers `LinkPrtgSSHAS`_.

.. _LinkPrtgSSHAS: https://www.paessler.com/manuals/prtg/ssh_script_advanced_sensor

