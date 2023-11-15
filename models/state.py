#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
import os
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    State class
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """
            Getter attribute cities that returns the list of
            City instances with state_id equals to the current State.id
            """
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
