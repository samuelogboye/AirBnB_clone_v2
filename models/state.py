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
    """State class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship(
            "City", cascade="all, delete, delete-orphan", 
            backref=backref("state", cascade="all, delete"),
            passive_deletes=True,
            single_parent=True
        )
    else:

        @property
        def cities(self):
            """getter attribute cities that returns
            the list of City instances"""
            from models import storage
            from models.city import City

            cities_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
