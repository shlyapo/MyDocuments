import os
from flask_bootstrap import Bootstrap
from flask import Flask

from views import IndexStart, Login

app = Flask(__name__, template_folder='templates')

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

app.add_url_rule('/', view_func=IndexStart.as_view('index_start'))
app.add_url_rule('/login', view_func=Login.as_view('login'))


if __name__ == '__main__':
    bootstrap = Bootstrap(app)
    app.run()
