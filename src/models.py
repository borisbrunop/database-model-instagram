import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    last_name = Column(String(250))
    enmail = Column(String(250), nullable=False)
    posts = relationship("Post", backref="author")
    notifications = relationship("Notification")
    inbox = relationship("Inbox", uselist=False)
    followers = relationship("Follower")
    histories = relationship("History")

#NOTIFICATION

class Notification(Base):
    __tablename__ = 'notification'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    fecha_hora = Column(DateTime, nullable=False)
    follow_request = Column(Boolean)

#FOLLOWER

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    follow = Column(Boolean)

#POST

class Post(Base):
    __tablename__= 'post'
    id = Column(Integer, primary_key=True)
    saved = Column(Boolean)
    fecha_hora = Column(DateTime, nullable=False)
    likes = Column(Integer)
    img = Column(String(250))
    coments = relationship("Comment")
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    like = relationship("Like", uselist=False)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    like = relationship("Like", uselist=False)


#LIKE

class Like(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    comment_id = Column(Integer, ForeignKey('comment.id'))
    message_id = Column(Integer, ForeignKey('message.id'))

#INBOX

class Inbox(Base):
    __tablename__ = 'inbox'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    chats = relationship("Chat")

class Chat(Base):
    __tablename__ = 'chat'
    id = Column(Integer, primary_key=True) 
    inbox_id = Column(Integer, ForeignKey('inbox.id'), nullable=False)

class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    img = Column(String)
    emoji = Column(String)
    gif = Column(String)
    history_id = Column(Integer, ForeignKey('history.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    chat_id = Column(Integer, ForeignKey('chat.id'), nullable=False)
    like = relationship("Like", uselist=False)



#HISTORY

class History(Base):
    __tablename__ = 'history'
    id = Column(Integer, primary_key=True)
    fecha_hora = Column(DateTime, nullable=False)
    status = Column(Boolean, nullable=False)
    destacados = Column(Boolean)
    img = Column(String)
    video = Column(String)
    message = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')