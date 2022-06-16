#!/usr/bin/python3
"""Holds State Class that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """Defines the State class

    Attributes:
        name (str) - The name of the state
    """

    name = ""
