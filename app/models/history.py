from sqlalchemy import Column, Integer, ForeignKey, DateTime, Text
from datetime import datetime
from .base import Base

class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True)
    domain_id = Column(Integer, ForeignKey("domains.id"))
    snapshot = Column(Text)  # store RDAP/WHOIS raw JSON or diff
    timestamp = Column(DateTime, default=datetime.utcnow)
