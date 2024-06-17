from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Grade
import settings

class Studentmanager:

    def __init__(self):
        self.engine = create_engine(settings.DATABASE_URL)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()