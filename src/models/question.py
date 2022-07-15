from uuid import uuid4
from datetime import datetime

from marshmallow import Schema, fields
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import String, Text, ARRAY, DateTime
from sqlalchemy import Column, PrimaryKeyConstraint, ForeignKeyConstraint, func
from sqlalchemy.orm import relationship

from src.models.base import BaseModel 


class Question(BaseModel):
    __tablename__ = 'question'

    id = Column(UUID(as_uuid=True), default=uuid4(), unique=True, nullable=False)
    text = Column(Text, nullable=False)
    options = Column(ARRAY(String), nullable=False)
    inserted_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=datetime.now)
    
    answer = relationship('Answer', back_populates='question', cascade="all, delete-orphan")


    __table_args__ = (
        PrimaryKeyConstraint(id),
    )


class QuestionSchema(Schema):
    id = fields.UUID()
    text = fields.String()
    options = fields.List(fields.String())
    inserted_at = fields.DateTime()
    updated_at = fields.DateTime()
    answer_id = fields.UUID()
