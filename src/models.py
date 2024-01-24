import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, LargeBinary
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    user_email = Column(String(30), nullable=False)
    user_tel = Column(String(13), nullable=False)
    user_privilege = Column(String(50), nullable=False)

class Admin(Base):
    __tablename__ = 'admin'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    admin_id = Column(Integer, primary_key=True)
    admin_name = Column(String(50), nullable=False)
    admin_email = Column(String(30), nullable=False)
    admin_tel = Column(String(13), nullable=False)
    admin_privilege = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)



class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    post_id = Column(Integer, primary_key=True)
    post_title = Column(String(250), nullable=False)
    post_text = Column(String(10250), nullable=False)
    post_photo = Column(LargeBinary)
    post_like = Column(Integer)
    post_comment = Column(String(500))
    post_favorite = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class WritePost(Base):
    __tablename__ = 'writepost'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), primary_key=True)
    user = relationship(User)    
    user = relationship(Post)

class SavePost(Base):
    __tablename__ = 'savepost'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), primary_key=True)
    post_title = Column(String(250), nullable=False)
    post_text = Column(String(10250), nullable=False)
    post_photo = Column(LargeBinary)
    post_like = Column(Integer)
    post_comment = Column(String(500))
    post_favorite = Column(Integer)
    user = relationship(User)    
    user = relationship(Post)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
