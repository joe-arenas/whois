from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    api_key = Column(String, unique=True, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    daily_quota = Column(Integer, default=10)
