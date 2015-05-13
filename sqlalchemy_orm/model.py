import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# Author: Matt Ankerson
# Date: 13 March 2015

Base = declarative_base()

# association table to address the many-many nature of Students and Papers
student_paper = Table('association', Base.metadata,
                      Column('student_id', Integer, ForeignKey('student.id')),
                      Column('paper_id', Integer, ForeignKey('paper.id')))


# student has a many-many relationship with paper
class Student(Base):
    __tablename__ = 'student'
    # define columns for table student
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    phone = Column(String(100), nullable=False)
    papers = relationship('Paper', secondary=student_paper, backref='students')


# semester has a one-many relationship with paper
class Semester(Base):
    __tablename__ = 'semester'
    # define columns for table semester
    id = Column(Integer, primary_key=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    papers = relationship("Paper", backref='semester')


class Paper(Base):
    __tablename__ = 'paper'
    # define columns for table paper
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    lecturer = Column(String, nullable=False)
    description = Column(String, nullable=True)
    semester_id = Column(Integer, ForeignKey('semester.id'))


# Create an engine that stores data in the local directory's
# sqlalchemy_students.db file.
engine = create_engine('sqlite:///sqlalchemy_students.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)