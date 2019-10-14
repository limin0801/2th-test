from pecan import expose
from q2_bbs.database.api import section as api_section
from q2_bbs.database.model import section as model_section


class SectionController(object):
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
        return self.section.delete_one_by_sectionname(section_name)
