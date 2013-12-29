
from framework import bottle, requests
from framework.bottle import Bottle, run, request, response
from framework.bottle import route, template, request, error, debug
#from google.appengine.ext.webapp.util import run_wsgi_app
from framework.douban_client import DoubanClient
from framework.douban_client.api import User

from framework.douban_client.pyoauth2 import Client
from framework.douban_client.pyoauth2 import AccessToken

import config


bottle = Bottle()

@bottle.route('/')
def home():
    DOUBAN_SCOPE = "douban_basic_common,community_basic_user,community_basic_online"
    print "# Init client with"
    print "- API KEY: %s" % config.DOUBAN_API_KEY
    print "- API SECRET: %s" % config.DOUBAN_API_SECRET
    print "- REDIRECT URI: %s" % config.DOUBAN_REDIRECT_URI 
    print "- SCOPE: %s" % DOUBAN_SCOPE
    client = DoubanClient(config.DOUBAN_API_KEY, config.DOUBAN_API_SECRET, config.DOUBAN_REDIRECT_URI, DOUBAN_SCOPE)


    # Option 1: Auth by code
    #print "Go to the following link in your browser: %s" % client.authorize_url
    #request = requests.post(client.authorize_url)
    #print request.text
    #code = config.DOUBAN_CODE
    #client.auth_with_code(code)
    
    # Option 2: Auth with exists token
    #token = config.DOUBAN_TOKEN
    #client.auth_with_token(token)

    # Option 3: Auth with user name & pwd
    #client.auth_with_password(
    #        config.DOUBAN_ROBOT_EMAIL,
    #        config.DOUBAN_ROBOT_PWD
    #        )
    #client.auth_with_password(config.DOUBAN_ROBOT_EMAIL, config.DOUBAN_ROBOT_PWD)
    #client.auth_with_password(config.DOUBAN_ROBOT_USERNAME, config.DOUBAN_ROBOT_PWD)
    client.auth_with_password(config.DOUBAN_ROBOT_USERID, config.DOUBAN_ROBOT_PWD)

    token_code = client.token_code
    print "- TOKEN: %s" % token_code

    refresh_token_code = client.refresh_token_code
    print "- REFRESH TOKEN: %s" % refresh_token_code

    print "- USER ME: %s" % client.user.me

    #access_token = client.access_token.token
    #print "- ACCESS_TOKEN: %s" % access_token

    '''
    refresh_token_code = client.refresh_token_code
    print "- REFRESH TOKEN: %s" % refresh_token_code
    refresh_token_code = config.DOUBAN_REFRESH_TOKEN
    print "- REFRESH TOKEN: %s" % refresh_token_code

    client.refresh_token(refresh_token_code)
    token_code = client.token_code
    print "- NEW TOKEN: %s" % token_code
    '''

    return client.discussion.comments(config.DOUBAN_ROBOT_COMMENT_TARGET_GROUP_TOPIC_ID)
    return req.text
    return req


@error(403)
def Error403(code):
    return "Get your codes right dude, you caused some error!"

                               
@error(404)
def Error404(code):
    return "Stop cowboy, what are you trying to find?"


#@bottle.route('/test')
#def test():
#    authorize_url = client.auth_code.authorize_url(redirect_uri=REDIRECT_URL, scope=SCOPE)


@bottle.route('/r060t')
def addComment():
    client = Client(
            config.DOUBAN_API_KEY,
            config.DOUBAN_API_SECRET,
            site='https://api.douban.com',
            authorize_url='https://www.douban.com/service/auth2/auth',
            token_url='https://www.douban.com/service/auth2/token'
            )
    access_token = client.password.get_token(
            config.DOUBAN_ROBOT_EMAIL,
            config.DOUBAN_ROBOT_PWD
            )
    print access_token
    print access_token.token

    print '-' * 80

    comment_url = "/v2/group/topic/%s/comments" % config.DOUBAN_ROBOT_COMMENT_TARGET_GROUP_TOPIC_ID
    #request = access_token.get(comment_url, alt='json')
    #request = access_token.get('/v2/group/topic/40792473/comment/582197675')
    content = "ROBOT TESTING"
    #request = access_token.post('/v2/group/topic/%s/comments/?content=ROBOTTEST' % config.DOUBAN_ROBOT_COMMENT_TARGET_GROUP_TOPIC_ID, data=content)
    #request = access_token.post('/v2/group/topic/%s#last/comments' % config.DOUBAN_ROBOT_COMMENT_TARGET_GROUP_TOPIC_ID, data=content)
    #request = access_token.post(comment_url, content=content)
    #request = access_token.get('/v2/book/1220562') # OK
    request = access_token.get('/v2/user/~me')
    print request.parsed

    return request.parsed

