#!/home/cdfcubas/djangoenv/bin/python
# Set up the virtual environment:
import os, sys
#open("/home/cdfcubas/public_html/cdfsite/my.log", "w").write("Before try")
#activate_this = "/home/cdfcubas/djangoenv/bin/activate_this.py"
#execfile(activate_this, dict(__file__=activate_this))
os.environ.setdefault('PATH', '/bin:/usr/bin')
os.environ['PATH'] = '/home/cdfcubas/djangoenv/bin:' + os.environ['PATH']
os.environ['VIRTUAL_ENV'] = '/home/cdfcubas/djangoenv/bin'
os.environ['PYTHON_EGG_CACHE'] = '/home/cdfcubas/djangoenv/bin'
os.chdir('/home/cdfcubas/public_html/cdfsite')
# Add a custom Python path.
#sys.path.insert(0, "/home/cdfcubas/djangoenv/bin/python")
sys.path.insert(0, "/home/cdfcubas/public_html/cdfsite")
# Set the DJANGO_SETTINGS_MODULE environment variable to the file in the # application directory with the db settings etc.
os.environ['DJANGO_SETTINGS_MODULE'] = "cdfsite.settings"
from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")