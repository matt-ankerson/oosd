from model import Student, Base, Paper, Semester
from sqlalchemy import create_engine
engine = create_engine('sqlite:///sqlalchemy_students.db')
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

# Author: Matt Ankerson
# Date: 14 March 2015

# list all students from the database
students = session.query(Student).all()
for s in students:
    print(s.name)

# list all papers from the database
papers = session.query(Paper).all()
for p in papers:
    print(p.title + ' | ' + p.lecturer + ' | ' + p.description)

# select a paper, see details for the paper and students enrolled.
paper = session.query(Paper).filter(Paper.title == 'oosd').first()
print('Chosen Paper: ' + paper.title)
print('Details: ' + paper.lecturer + ' | ' + paper.description)
# print out students
for s in paper.students:
    print(s.name)

# select a student and a semester, show the student's papers for that semester
student = session.query(Student).first()    # just select the first ones
semester = session.query(Semester).first()
papers_scheduled = session.query(Paper, Student).filter(and_(Paper.semester_id == semester.id), (Paper.students.any(Student)))
# print out papers scheduled
print(student.name + ' for semester ' + str(semester.id) + ':')
for ps in papers_scheduled:
    print(ps.title)

