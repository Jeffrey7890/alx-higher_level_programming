#!/usr/bin/python3
""" create class fo state """
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine


Base = declarative_base()


class State(Base):
    """ class state """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False, unique=True)
