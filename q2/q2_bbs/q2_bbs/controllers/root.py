from q2_bbs.controllers import user
from q2_bbs.controllers import section

class RootController(object):
    user = user.UserController()
    section = section.SectionController()
