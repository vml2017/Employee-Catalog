from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from database_setup import User, Employee, Base

engine = create_engine('sqlite:///uemployeecatlog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

#Create dummy user
User1 = User(name="Tom Gore", email="TomG@eagles.com",
             picture=r"images/eagles.png")
session.add(User1)
session.commit()

User2 = User(name="Udacity Review", email="udacity.review2018@gmail.com",
             picture=r"images/eagles.png")
session.add(User2)
session.commit()

print('User record added')
