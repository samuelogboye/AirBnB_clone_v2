#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
import models

if getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column(
            "place_id",
            String(60),
            ForeignKey("places.id"),
            primary_key=True,
            nullable=False,
        ),
        Column(
            "amenity_id",
            String(60),
            ForeignKey("amenities.id"),
            primary_key=True,
            nullable=False))


class Place(BaseModel, Base):
    """A Place Class to stay"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        reviews = relationship(
            "Review", cascade="all, delete", backref="places"
        )
        amenities = relationship(
            "Amenity",
            secondary='place_amenity',
            viewonly=False,
            back_populates="place_amenities"
        )

    else:
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

    def __init__(self, *args, **kwargs):
        """Initializes a new Place"""
        super().__init__(*args, **kwargs)

    @property
    def reviews(self):
        """getter attribute cities that returns
            the list of City instances"""
        reviews_list = []
        for review in models.storage.all("Review").values():
            if review.place_id == self.id:
                reviews_list.append(review)
        return reviews_list

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def amenities(self):
            """getter attribute cities that returns
            the list amenity ids"""
            list_amenities = []
            for amenity in models.storage.all("Amenity").values():
                if amenity.id in self.amenity_ids:
                    list_amenities.append(amenity)
            return list_amenities
