from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Grade, Course
import settings

class Studentmanager:

    def __init__(self):
        self.engine = create_engine(settings.DB_address)
        # self.Session = sessionmaker(bind=self.engine)
        # self.session = self.Session()
    
    @property
    def get_session(self):
        """Create new session with current engine."""
        return sessionmaker(bind=self.engine)()
    
    # add behaviour of adding students
    def add_student(self, name, surname, date_of_birth, email, phone_number):
        # create student object
        new_student = Student(name=name, 
                              surname=surname, 
                              date_of_birth=date_of_birth, 
                              email=email, 
                              phone_number=phone_number)
        # add student object to session
        with self.get_session as session:
            session.add(new_student)
            session.commit()
    
    # add behaviour for removing student
    def remove_student(self, student_id):
        with self.get_session as session:
            student = session.query(Student).filter(Student.id == student_id).first()
            session.delete(student)
            session.commit()
    
    # add behaviour to get student by id
    def get_student(self, student_id):
        with self.get_session as session:
            result = session.query(Student).filter(Student.id == student_id).first()
            return str(result)
    
    # add behaviour to update student email
    def update_email(self, student_id, email):
        with self.get_session as session:
            student = session.query(Student).filter(Student.id == student_id).first()
            student.email = email
            session.query(Student).filter(Student.id == student_id).first()
            session.commit()

    # add behaviour to view all student
    def view_all_students(self):
        with self.get_session as session:
            result = session.query(Student).all()
            for student in result:
                print(f"{student.name} {student.surname} - {student.email} - {student.phone_number}")

    # add behaviour to add_grade
    def add_grade(self, student_id, subject, grade, course_id):
        new_grade = Grade(student_id=student_id, 
                          subject=subject, 
                          grade=grade, 
                          course_id=course_id)
        with self.get_session as session:
            result = session.query(Grade).filter(Grade.student_id == student_id, Grade.subject == subject).first()
            if result:
                session.add(new_grade)
                session.commit()
            

# testing purposes
from datetime import date
test=Studentmanager()
# test.add_student("John", "Doe", date(1990, 1, 1), "test@gmail.com", "07570810555")
# test.add_student("Jane", "Doe", date(1990, 1, 1), "demo@gmail.com", "07570810556")
#test.add_grade(12, "english", 9, 12)
test.view_all_students()
print(test.get_student(12))