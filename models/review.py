#!/usr/bin/python
""" holds class Review"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """representation of review"""
    if models.storage_db == 'db':
        __tablename__ = 'review'
        place_id = Column(String(60), ForeignKey('place_id'), nullable=False)
        user_id = Column(String(60), ForeignKey('user_id'), nullable=False)
        text = Column(String(1024, nullable=False))
    else:
        place_id = ""
        user_id = ""
        text = ""
        
    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)