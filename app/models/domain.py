from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .base import Base

class Domain(Base):
    __tablename__ = "domains"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    last_checked = Column(DateTime, default=datetime.utcnow)
    last_status = Column(String, nullable=True)
