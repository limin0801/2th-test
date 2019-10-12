from pecan import expose
from pecan import response
from q2_bbs.database.api import section as api_section
from q2_bbs.database.api import user as api_user
from q2_bbs.database.model import section as model_section
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
        self.user.delete_one_by_username(user_name)
        return None

    @expose(method='GET')
    def login(self, user):
        result = self.user.login(user)
        response.text = result


class RootController(object):
    def __init__(self):
        self.section = api_section.SectionAPI()

    @expose(generic=True, template='json')
    def index(self):
        return self.section.get_all()

    @expose(method='GET', template='json')
    def show(self, sectionname):
        return self.section.get_one_by_section_name(sectionname)

    @expose(method='POST', template='json')
    def post(self, section):
        section = model_section.Section(**section)
        return self.section.add_one(section)

    @expose(method='DELETE', template='json')
    def delete(self, section_name):
        self.section.delete_one_by_sectionname(section_name)
        return None

    user = UserController()
