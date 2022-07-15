from uuid import uuid4
from datetime import datetime

from marshmallow import Schema, fields
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import String, Text, ARRAY, DateTime
from sqlalchemy import Column, ForeignKeyConstraint, PrimaryKeyConstraint, func
from sqlalchemy.orm import relationship

from src.models.base import BaseModel 


class Answer(BaseModel):
    __tablename__ = 'answer'

    id = Column(UUID(as_uuid=True), default=uuid4(), unique=True, nullable=False)
    text = Column(Text, nullable=False)
    inserted_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=datetime.now)
    question_id = Column(UUID(as_uuid=True), nullable=False)
    
    question = relationship('Question', back_populates='answer', uselist=False, cascade="all, delete")
    

    __table_args__ = (
        PrimaryKeyConstraint(id),
        ForeignKeyConstraint(
            (question_id,), 
            ('question.id',),
            ),
    )


class AnswerSchema(Schema):
    id = fields.UUID()
    text = fields.String()
    inserted_at = fields.DateTime()
    updated_at = fields.DateTime()
    question_id = fields.UUID()
    