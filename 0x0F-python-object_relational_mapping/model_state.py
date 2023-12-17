#!/usr/bin/python3
"""
contains the class definition of a State and an
instance Base = declarative_base()
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    a class defining State
    """
    __tablename__ = "states"

    id = Column(
            Integer, primary_key=True, autoincrement=True, unique=True,
            nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name
