from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'  # Cambié el nombre de la tabla para evitar conflictos
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    firstname = Column(String(50), nullable=False)
    secondname = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    comments = relationship('Comment', backref='user', lazy=True)
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "secondname": self.secondname,
            "email": self.email,
        }
class Comment(db.Model):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(50), nullable=False)
    author_id = Column(Integer, nullable=False)
    post_id = Column(Integer, nullable=False)

    def serialize(self):
        return {
             "comment_text": self.comment_text,
             "author_id": self.author_id,
             "post_id": self.post_id,
        }
    
class Post (db.Model):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)

def serialize(self):
        return {
             "user_id": self.user_id,
        }

class Media (db.Model):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum("image", name="media_types"))
    url = Column(String)
    post_id = Column(Integer, nullable=False)
def serialize(self):
        
        return {
            "id": self.id,
            "type": self.type,
            "url": self.url,
            "post_id": self.post_id    
        }

class Follower (db.Model):
     __tablename__ = 'media'
     user_from_id = Column(Integer, primary_key=True)
     user_to_id = Column(Integer)

def serialize(self):
     return {
        user_from_id: self.user_from_id,
        user_to_id: self.user_to_id
     }

