from flask import Flask, redirect, request
from douban_client import DoubanClient

import re
import mechanize
import cookielib


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# config
KEY = config.DOUBAN_API_KEY
SECRET = config.DOUBAN_API_SECRET
CALLBACK = 'http://127.0.0.1:5000/callback'
SCOPE = 'douban_basic_common,community_basic_user'

app = Flask(__name__)
client = DoubanClient(KEY, SECRET, CALLBACK, SCOPE)


@app.route('/')
def home():
    return '<a href="/auth">Auth</a>'


@app.route('/auth')
def auth():
    return redirect(client.authorize_url)
    #browser = mechanize.Browser()
    #browser.set_handle_robots(False)

    #browser.open(client.authorize_url)
    #print "AUTH"
    #browser.submit()


@app.route('/callback')
def callback():
    print "CALL BACK"
    code = request.args.get('code')
    client.auth_with_code(code)
    #print client.discussion.comments(config.DOUBAN_ROBOT_COMMENT_TARGET_GROUP_TOPIC_ID)
    return str(client.user.me)


@app.route('/m')
def mech():
    login_url = "http://www.douban.com/login" 
    #comment_url = "http://www.douban.com/group/topic/%s/?cid=%s#last" % (config.DOUBAN_ROBOT_COMMENT_TARGET_GROUP_TOPIC_ID, DOUBAN_ROBOT_COMMENT_TARGET_GROUP_TOPIC_FIRST_COMMENT_ID)
    #comment_url = "http://www.douban.com/group/topic/%s/?start=100&post=ok#last" % config.DOUBAN_ROBOT_COMMENT_TARGET_GROUP_TOPIC_ID
    comment_url = "http://www.douban.com/group/topic/%s/?start=100" % config.DOUBAN_ROBOT_COMMENT_TARGET_GROUP_TOPIC_ID

    browser = mechanize.Browser()
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    cj = cookielib.CookieJar()
    browser.set_cookiejar(cj)
    #browser.set_handle_robots(False)

    #
    # Login
    #
    browser.open(login_url)
    print ">>> TITLE: %s" % browser.title()

    # Select the login form
    #for f in browser.forms():
    #    print f
    browser.select_form(nr=0)
    #for f in browser.forms():
    #    print f

    # Populate email & pwd
    browser.form["form_email"]    = config.DOUBAN_ROBOT_EMAIL
    browser.form["form_password"] = config.DOUBAN_ROBOT_PWD
    browser.submit()
    print browser._ua_handlers['_cookies'].cookiejar

    #
    # Add comment
    #
    browser.open(comment_url)
    print ">>> TITLE: %s" % browser.title()

    #for f in browser.forms():
    #    print f
    browser.form = list(browser.forms())[1]
    browser.form.set_all_readonly(False)
    print ">>> set_all_readonly FALSE"

    #for control in browser.form.controls:
    #    print "%s: type=%s, name=%s value=%s" % (control, control.type, control.name, browser[control.name])

    print "-" * 80
    browser.form["rv_comment"] = "TESTING"
    #browser.form["sync_to_mb"].selected = True
    #browser.find_control["sync_to_mb"].items[0].selected = True

    for control in browser.form.controls:
        print "%s: type=%s, name=%s value=%s" % (control, control.type, control.name, browser[control.name])

    print "-" * 80
    #browser.form.click(name="submit_btn",nr=0)
    #browser.form.action="add_comment#last"
    #browser.form.onsubmit="this.onsubmit=function(){return true}"
    #print browser.response().read()
    print browser._ua_handlers['_cookies'].cookiejar
    browser.submit()
    print ">>> DONE"
    print "-" * 80
    print browser.response().read()
    return
    browser.submit()
 
    # puts agent.cookie_jar.inspect
    #page = agent.get(comment_url)
    #comment_form = page.forms.last
    #comment_form.rv_comment = "ROBOT TESTING"
    #page = agent.submit(comment_form)
    #print page.body
    return

@app.route('/s')
def sele():
    login_url = "http://www.douban.com/login" 
    browser = webdriver.Firefox()
    browser.get(login_url)
    form = browser
    browser.find_element_by_name("form_email").clear()
    browser.find_element_by_name("form_email").send_keys(config.DOUBAN_ROBOT_EMAIL)
    browser.find_element_by_name("form_password").clear()
    browser.find_element_by_name("form_password").send_keys(config.DOUBAN_ROBOT_PWD)
    print ">>> CHECK"
    return
    


@app.route('/robot')
def robot():
    #code = request.args.get('code')
    #client.auth_with_code(code)
    #client.auth_with_password(config.DOUBAN_ROBOT_EMAIL, config.DOUBAN_ROBOT_PWD)
    client.auth_with_password(config.DOUBAN_ROBOT_USERNAME, config.DOUBAN_ROBOT_PWD)
    #client.auth_with_password(config.DOUBAN_ROBOT_USERID, config.DOUBAN_ROBOT_PWD)
    #print client.discussion.comments(config.DOUBAN_ROBOT_COMMENT_TARGET_GROUP_TOPIC_ID)
    return str(client.user.me)


if __name__ == '__main__':
    app.run()

