#!/home/cdfcubas/djangoenv/bin/python

import sys

from flup.server.fcgi_fork import WSGIServer

def myapp(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello World!\n']

if __name__ == '__main__':
    WSGIServer(myapp).run()