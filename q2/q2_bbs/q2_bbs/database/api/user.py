from sqlalchemy import orm, exc

from q2_bbs import database
from q2_bbs.database.model import user as model_user

import hashlib


class UserAPI(object):
    def get_one_by_username(self, username):
        session = database.get_session()
        query = session.query(model_user.User).filter_by(name=username)
        try:
            user = query.one()
            return user
        except orm.exc.NoResultFound:
            return None

    def get_all(self):
        session = database.get_session()
        query = session.query(model_user.User)
        try:
            users = query.all()
            return users
        except orm.exc.NoResultFound:
            return None

    def add_one(self, user):
        session = database.get_session()
        md5 = hashlib.md5()
        md5.update(user.passwd.encode('utf-8'))
        user.passwd = md5.hexdigest()
        try:
            session.add(user)
            session.flush()
            session.commit()
            return user
        except exc.IntegrityError:
            str = "User is exist!"
            return str

    def delete_one_by_username(self, username):
        session = database.get_session()
        query = session.query(
            model_user.User).filter_by(name=username)
        try:
            user = query.one()
            session.delete(user)
            session.flush()
            session.commit()
            return user
        except orm.exc.NoResultFound:
            str = "User is not exist!"
            return str

    def login(self, user):
        session = database.get_session()
        query = session.query(model_user.User).filter_by(name=user["name"])
        try:
            user_origin = query.one()
        except orm.exc.NoResultFound:
            str = "User dose not exist"
            return str

        md5 = hashlib.md5()
        md5.update(user["passwd"].encode('utf-8'))
        user_password = md5.hexdigest()

        if user_password == user_origin.passwd:
            if user_origin.admin:
                str = "Welcome, admin!"
            else:
                str = "You are not an administrator and \
do not have permission to perform this operation."
        else:
            str = "Your username or password is incorrect. Please try again."
        return str
