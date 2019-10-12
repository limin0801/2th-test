from sqlalchemy.orm import exc

from q2_bbs import database
from q2_bbs.database.model import section as model_section


class SectionAPI(object):
    def get_one_by_section_name(self, sectionname):
        session = database.get_session()
        query = session.query(
            model_section.Section).filter_by(name=sectionname)
        try:
            section = query.one()
            return section
        except exc.NoResultFound:
            return None

    def get_all(self):
        session = database.get_session()
        query = session.query(model_section.Section)
        try:
            sections = query.all()
            return sections
        except exc.NoResultFound:
            return None

    def add_one(self, section):
        session = database.get_session()
        try:
            session.add(section)
            session.flush()
            session.commit()
            return section
        except Exception:
            pass

    def delete_one_by_sectionname(self, sectionname):
        session = database.get_session()
        query = session.query(
            model_section.Section).filter_by(name=sectionname)
        reply = input(
            "Are you sure to delete the section? (y/n)")
        if reply == 'y':
            try:
                section = query.first()
                session.delete(section)
                session.flush()
                session.commit()
            except exc.NoResultFound:
                pass
        elif reply == 'n':
            return None
        else:
            print("Please input y or n")
