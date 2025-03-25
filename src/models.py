from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'  # Cambié el nombre de la tabla para evitar conflictos

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)3

    conection_comment = relationship("Comment", back_populates="conection_user")
    conection_follower = relationship("Follower", "conection_user2")

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "secondname": self.secondname,
            "email": self.email,
        }
    

class Comment(db.Model):
    __tablename__ = 'Comments'

    id = Column(Integer, primary_key=True)
    comment_text = Column(String(50), nullable=False)
    author_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("post.id") nullable=False)

    conection_user = relationship("User", back_populates="conection_comment")
    conection_post = relationship("Post", back_populates="conection_comment2")

    def serialize(self):
        return {
             "comment_text": self.comment_text,
             "author_id": self.author_id,
             "post_id": self.post_id,
        }
    
    
class Post (db.Model):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id") nullable=False)

    conection_comment2 = relationship("Comment", "conection_post")
    conection_media = relationship("Media", "conection_post2")

def serialize(self):
        return {
             "user_id": self.user_id,
        }

class Media (db.Model):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum("image", name="media_types"))
    url = Column(String)
    post_id = Column(Integer, ForeignKey("post.id") nullable=False)

    conection_post2 = relationship("Post", "conection_media")

def serialize(self):
        
        return {
            "id": self.id,
            "type": self.type,
            "url": self.url,
            "post_id": self.post_id    
        }

class Follower (db.Model):
     __tablename__ = 'media'
     user_from_id = Column(Integer, ForeignKey("user.id") primary_key=True)
     user_to_id = Column(Integer, ForeignKey("user.id"))

     conection_user2 = relationship("User", "conection_follower")


def serialize(self):
     return {   
        "user_from_id": self.user_from_id,
        "user_to_id": self.user_to_id
     }

