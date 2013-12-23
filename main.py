
from framework import bottle
from framework.bottle import Bottle, run, request, response
from framework.bottle import route, template, request, error, debug
#from google.appengine.ext.webapp.util import run_wsgi_app

bottle = Bottle()

@bottle.route('/')
def home():
    return "Douban Robot"

@error(403)
def Error403(code):
    return 'Get your codes right dude, you caused some error!'
                               
@error(404)
def Error404(code):
    return 'Stop cowboy, what are you trying to find?'

@bottle.route('/r060t')
def addComment():
    return "Add Comment"

