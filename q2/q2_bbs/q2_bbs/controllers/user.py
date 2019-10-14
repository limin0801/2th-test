from pecan import expose
from q2_bbs.database.api import user as api_user
from q2_bbs.database.model import user as model_user


class UserController(object):
    def __init__(self):
        self.user = api_user.UserAPI()

    @expose(method='GET', template='json')
    def index(self):
        return self.user.get_all()

    @expose(method='GET', template='json')
    def show(self, username):
        return self.user.get_one_by_username(username)

    @expose(method='POST', template='json')
    def post(self, user):
        user = model_user.User(**user)
        return self.user.add_one(user)

    @expose(method='DELETE', template='json')
    def delete(self, user_name):
        return self.user.delete_one_by_username(user_name)

    @expose(method='GET')
    def login(self, user):
        return self.user.login(user)
