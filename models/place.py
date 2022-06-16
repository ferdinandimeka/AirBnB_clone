#!/usr/bin/python3
"""Holds User class that inherits from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Initializes the Place class

    Attributes:
        city_id (str) - Refers to the City.id
        user_id (str) - Refers to the User.id
        name (str) - The name of the place
        description (str) - A description of the place
        number_rooms (int) - The number of rooms
        number_bathrooms (int) - The number of bathrooms
        max_guest (int) - The maximum number of guests allowed
        price_by_night (int) - The cost of a night
        latitude (float) - The latitude location of the place
        longitude (float) - The longitude location of the place
        amenity_ids (list of str) - List of Amenity.id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
