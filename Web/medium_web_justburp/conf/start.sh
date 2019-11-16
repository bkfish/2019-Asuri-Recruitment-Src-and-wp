#!/bin/sh
a2enmod rewrite
mv /tmp/conf /etc/apache2/apache2.conf
/etc/init.d/apache2 start
rm -f /var/www/html/index.html
unzip /var/www/html/www.zip -d /var/www/html
rm -rf /var/www/html/__MACOSX
rm -rf /var/www/html/www.zip
rm -rf /var/www/html/.DS_Store
chmod 755 -R /var/www/html

/bin/bash
