from sqlalchemy import Column, String, Boolean
from q2_bbs.database import Base


class User(Base):
    __tablename__ = 'users'
    name = Column(String(20), primary_key=True)
    passwd = Column(String(32))
    admin = Column(Boolean())

    def __json__(self):
        return dict(
            username=self.name,
            password="****",
            admin=self.admin,
        )
