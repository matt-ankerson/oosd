from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date

from model import Semester, Student, Paper, Base

engine = create_engine('sqlite:///sqlalchemy_students.db')
# Bind the engine to the metadata of the Base class so that the
# model can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object.
session = DBSession()

# create and insert Semesters
semester_1 = Semester(start_date=date(2015, 2, 16), end_date=date(2015, 6, 19))
session.add(semester_1)
semester_2 = Semester(start_date=date(2015, 7, 16), end_date=date(2015, 11, 19))
session.add(semester_2)

session.commit()

# create Papers
oosd = Paper(title='oosd', lecturer='Tom', description='Hacky OO Python', semester_id='0')

web3 = Paper(title='web3', lecturer='Davo', description='Client side stuff', semester_id='0')

mobile = Paper(title='mobile', lecturer='Pat', description='Design and dev for Android', semester_id='0')

project_1 = Paper(title='project_1', lecturer='Sam', description='Sams holiday', semester_id='0')

db3 = Paper(title='db3', lecturer='Davo', description='Wicked data science stuff', semester_id='1')

ads = Paper(title='ads', lecturer='Tom', description='Algorithms and other nasties', semester_id='1')

project_2 = Paper(title='project_2', lecturer='Sam', description='Sams second holiday', semester_id='1')


# create Students, append papers as necessary, insert Students and Papers
student_1 = Student(name='Matt', phone='234321')
student_1.papers.extend([oosd, web3, mobile, project_1, db3, ads, project_2])
student_2 = Student(name='Sam', phone='987865')
student_2.papers.extend([oosd, mobile, project_1, db3, ads, project_2])
student_3 = Student(name='Alex', phone='546753')
student_3.papers.extend([oosd, web3, mobile, project_1, db3, ads, project_2])
student_4 = Student(name='Nige', phone='723478')
student_4.papers.extend([project_1, db3, ads, project_2])

session.add_all([student_1, student_2, student_3, student_4])
session.commit()