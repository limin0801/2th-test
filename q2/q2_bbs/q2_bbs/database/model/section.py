from sqlalchemy import Column, String, Text
from q2_bbs.database import Base


class Section(Base):
    __tablename__ = 'section'
    name = Column(String(20), primary_key=True)
    description = Column(Text)

    def __json__(self):
        return dict(
            sectionname=self.name,
            description=self.description,
        )
