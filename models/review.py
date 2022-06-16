#!/usr/bin/python3
"""Holds User class that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Initalizes Review class

    Attributes:
        place_id (str) - Refers to the Place.id
        user_id (str) - Refers to the User.id
        text (str) - The content of the review
    """

    place_id = ""
    user_id = ""
    text = ""
