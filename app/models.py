"""Models DB"""
import datetime

from passlib.hash import pbkdf2_sha256 as sha256
from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import base, session


class UserModel(base):
    """User DB Model"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    deleted = Column(Boolean, default=False)
    email = Column(String(128), nullable=False)
    name = Column(String(64), nullable=False)
    hashed_password = Column(String(128), nullable=False)
    groups = relationship("GroupModel")
    posts = relationship("PostModel")

    @classmethod
    def get_first(cls, filters: dict = None):
        """Get user by filters"""
        query = (
            session.query(cls).filter_by(**filters) if filters else session.query(cls)
        )
        return query.first()

    @classmethod
    def get_all(cls, filters: dict = None, offset: int = 0, limit: int = 100):
        """Get query of users by filters with offset and limit"""
        query = (
            session.query(cls).filter_by(**filters) if filters else session.query(cls)
        )
        return (
            query.filter_by(**{"deleted": False})
            .order_by(cls.id)
            .offset(offset)
            .limit(limit)
            .all()
        )

    def save(self):
        """Add user with group 'reader' to DB"""
        session.add(self)
        session.commit()

    def delete(self):
        """Mark user for deleting"""
        self.deleted = True
        self.save()

    def to_dict(self):
        """Represent user to dict"""
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "hashed_password": self.hashed_password,
            "posts": [p.text for p in self.posts if not p.deleted],
        }

    @staticmethod
    def generate_hash(password):
        """Hash user's password"""
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        """Verify user's password"""
        return sha256.verify(password, hash)

