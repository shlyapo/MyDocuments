from flask.views import MethodView

from forms import LoginForm
from nav import *
from db import collection, collection_contracts, collection_partners, DbHelper
from flask import request, redirect, json, render_template, session, url_for
from functions import employee_functions


############################## <!----! Пользователи  !----!>

class IndexStart(MethodView):
    def get(self):
        return render_template('index_start.html',
                               title='Home')


class IndexUser(MethodView):
    def get(self):
        return render_template('index.html',
                               title='Home')


class Login(MethodView):
    def get(self):

        if session.get('login'):
            return redirect(url_for('index'))

        login_form = LoginForm()
        return render_template('login.html',
                               title='Login',
                               login_form=login_form,
                               session=session.get('login'))

    def post(self):

        login_form = LoginForm()

        if login_form.validate_on_submit():
            db = DbHelper()
            user = db.find_document(db.user_collection, {'password': login_form.password.data,
                                                         'login': login_form.login.data})
            if user is None:
                # todo not_exist_template
                return redirect(url_for('login'))
            elif user.password == login_form.password.data:
                pass


class Logout(MethodView):

    def get(self):
        session.pop('login', None)
        return redirect(url_for('index_start'))
