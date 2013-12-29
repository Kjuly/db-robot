from flask import Flask, redirect, request
from douban_client import DoubanClient

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


@app.route('/callback')
def callback():
    code = request.args.get('code')
    client.auth_with_code(code)
    #print client.discussion.comments(config.DOUBAN_ROBOT_COMMENT_TARGET_GROUP_TOPIC_ID)
    return str(client.user.me)


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

