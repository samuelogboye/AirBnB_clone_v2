#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from os import getenv
from models.city import City
import models


class State(BaseModel, Base):
    """The State class"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City", backref="states", cascade="all, delete, delete-orphan"
        )
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initialize the State"""
        super().__init__(*args, **kwargs)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        @property
        def cities(self):
            """getter attribute cities that returns
            the list of City instances"""
            cities_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
