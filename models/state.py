#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", cascade="all, delete, delete-orphan", backref="state")

    @property
    def cities(self):
        """getter attribute cities that returns the list of City instances"""
        from models import storage
        from models.city import City
        cities_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list
    """
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            from models import storage, City
            return [city for city in storage.all(City).values()
                    if city.state_id == self.id]
    """