from sqlalchemy import MetaData
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage:
    '''
    Database storage engine
    '''
    __engine = None
    __session = None
    def __init__(self):
        '''DBstorage instances'''
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db_name = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine(f"mysql+mysqldb://{user}:{pwd}@{host}/{db_name}", pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(bind=self.__engine)
    
    def all(self, cls=None):
        
    def new(self, obj):
        if obj:
            self.__session.add(obj)
    def save(self):
        self.__session.commit()   

    def delete(self, obj=None):
        self.__session.delete(obj)
    
    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        self.__session.close()
