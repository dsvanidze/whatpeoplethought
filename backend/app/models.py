from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class Thought(Base):
    __tablename__ = "thoughts"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
