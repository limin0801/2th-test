from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import exc

import hashlib
import sys

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    name = Column(String(20), primary_key=True)
    passwd = Column(String(32))


engine = create_engine('mysql+pymysql://root:root@localhost:3306/test')
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Base.metadata.create_all(engine)


if __name__ == '__main__':
    user_name = sys.argv[1]
    user_password = sys.argv[2]

    md5 = hashlib.md5()
    md5.update(user_password.encode('utf-8'))
    user_password = md5.hexdigest()

    try:
        user = session.query(User).filter_by(name=user_name).one()
    except exc.NoResultFound:
        user = None
        print("User does not exist!")

    if user:
        if user.passwd == user_password:
            print("Welcome")
        else:
            print("Your username or password is incorrect. Please try again.")
