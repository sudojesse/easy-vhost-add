#!/usr/bin/env python

import os

name = raw_input('Enter the name of your desired virtual host, followed by [ENTER]: ')



# 1) look for desired name /etc/apache2/extra/httpd-vhosts.conf

# 2) if it exists, alert the user, otherwise, add the stuff
if name in open('/etc/apache2/extra/httpd-vhosts.conf').read():
	print 'vhost already exists. Please choose a different name.'
else:
	docRoot = raw_input('Enter the document root of the new virtual host, followed by [ENTER]: ')
	#if the directory does NOT exist, create it
	if not os.path.isdir(docRoot):
		os.mkdir(docRoot)
		#make an html file
		os.chdir(docRoot)
		with open('index.html', 'wb') as index:
			index.write('hello world!')
	#add the stuff to /etc/apache2/extra/httpd-vhosts.conf
	vhosts = open('/etc/apache2/extra/httpd-vhosts.conf', 'a')
	vhosts.write('<VirtualHost *:80>\n')
	vhosts.write("		DocumentRoot "+docRoot+'\n')
	vhosts.write("		ServerName "+name+'\n')
	vhosts.write("</VirtualHost>\n")
	vhosts.close()
	print 'added config to /etc/apache2/extra/httpd-vhosts.conf'
	
	#add the stuff to /etc/hosts
	with open('/etc/hosts', 'a') as hosts:
		config='127.0.0.1	'+name+'\n'
		hosts.write(config)
		print 'added config to /etc/hosts'
	
	#restart apache
	os.system('sudo apachectl restart')
	
	#open the docRoot in a web browser
	os.system('open http://'+name)