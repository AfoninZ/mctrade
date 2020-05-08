import os

from flask import Flask
from data import db_session
from data import users

app = Flask(__name__)


@app.route("/")
def index():
    return "mctrade is up and running!"

@app.route("/user/new/<username>")
def new_user(username):
    session = db_session.create_session()
    user = users.User()
    user.name = username
    session.add(user)
    session.commit()
    return 'added user'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    db_session.global_init("db/mctrade.sqlite")
    
    app.run(host='0.0.0.0', port=port)
