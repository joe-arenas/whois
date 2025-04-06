from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime
from .base import Base

class Lookup(Base):
    __tablename__ = "lookups"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    domain_id = Column(Integer, ForeignKey("domains.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
