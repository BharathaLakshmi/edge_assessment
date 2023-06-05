import uuid
from datetime import datetime
from .database import Base
from sqlalchemy import TIMESTAMP, Column, String,  Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class Source(Base):
    __tablename__ = 'source_info'
    source_id = Column(Integer, primary_key=True)
    source = Column(String,  nullable=False)
    source_type = Column(String, unique=True, nullable=False)
    source_tag = Column(String, nullable=False)
    last_update_date = Column(DateTime, nullable=False, default=datetime.now())
    from_date = Column(DateTime, nullable=False)
    to_date = Column(DateTime, nullable=False)
    frequency = Column(String, nullable=False)


