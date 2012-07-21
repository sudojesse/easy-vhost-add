#Easy Virtual Host Creation for Mac OS X

##Usage

Make sure `http-vhosts.conf` is included in `/etc/apache2/httpd.conf`

    $ sudo nano /etc/apache2/httpd.conf
    
around line #460, remove '#' from `#Include /private/etc/apache2/extra/httpd-vhosts.conf`


    $ git clone https://github.com/sudojesse/easy-vhost-add.git #clone the repo
    $ cd easy-vhost-add #move into the directory
    $ chmod +x new-vhost.py #make it executable
    $ sudo ./new-vhost.py #execute and enjoy!
    