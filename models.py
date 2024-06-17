from sqlalchemy.orm import declarative_base, relationship
# declarative_base() is a factory function that constructs a base class for declarative class definitions.
from sqlalchemy import Column, String, Integer, Date, ForeignKey
# Column is a class that constructs a column in a database table.

Base = declarative_base()
# Base is a class object from which all mapped classes should inherit.

class BaseModel(Base):# BaseModel is a class that inherits from Base.
    """Base model for other models."""
    __abstract__ = True # make this class abstract
    __allow__unmapped__ = True # allow this class to be used without being mapped to a table

    id = Column("id", Integer, autoincrement=True, primary_key=True)
    # id is a column in the database table that is an integer, autoincremented, and a primary key.

# model for grades
class Grade(BaseModel): # Grade is a class that inherits from BaseModel.
    __tablename__ = "Grades" # name of the table in the database
    grade = Column("grade", Integer, nullable=False)
    student_id = Column("student_id", Integer, ForeignKey("Students.id"), nullable=False) # foreign key to students table
    subject = Column("subject", String, nullable=False)
    course_id = Column("course_id", Integer, ForeignKey("Courses.id"), nullable=False)

    # for testing purposers use __repr__ to return a string representation of the object
    def __repr__(self):
        return f"<{self.subject} - {self.grade}%>"

# model for courses
class Course(BaseModel):
    __tablename__ = "Courses" # name of the table in the database
    name = Column("name", String, nullable=False)
    description = Column("description", String)
    teacher = Column("teacher", String)

# model for students 
class Student(BaseModel):
    __tablename__ = "Students" # name of the table in the database
    name = Column("name", String(100), nullable=False)
    surname = Column('surname', String, nullable=False)
    date_of_birth = Column('address', Date)
    email = Column('email', String)
    phone_number = Column("phone_number", String)
    grades = relationship(Grade)# grades is a relationship between the Student and Grade models
    courses = relationship(Course) # courses is a relationship between the Student and Course models

    # for testing purposers use __repr__ to return a string representation of the object
    def __repr__(self):
        return f"<{self.id} - ({self.name} {self.surname}) {self.grades = } {self.courses = }>"


    