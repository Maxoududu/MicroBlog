- How to install

We are using django 1.3.4 for this project available at https://www.djangoproject.com/download/1.3.4/tarball/

To install Django : 

tar xzvf Django-1.3.4.tar.gz
cd Django-1.3.4
sudo python setup.py install

We also using Mysql and picture libraries for Python :

sudo apt-get install python-mysqldb python-imaging


Make sure to adapt your settings.py with your database name, and correct the path for uploaded media (if needed)

to run the development server just launch launch in the site folder :
python manage.py runserver 0.0.0.0:4242

to use django with nginx you can follow this great tutorial : http://www.dmclaughlin.com/2008/11/03/complete-guide-to-deploying-django-on-ubuntu-with-nginx-fastcgi-and-mysql/

- The project

Please read the PDF...

- Credit

We used several tutos on the web (can't remember all of them) to do this project and allowing us to discover and enjoy the incredible possibilities of python.