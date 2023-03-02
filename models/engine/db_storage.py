#!/usr/bin/python3
from os import getenv
from models.base_model import Base, BaseModel
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBStorage:
    __engine = None
    __session = None
    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                            .format(getenv('HBNB_MYSQL_USER'),
                                    getenv('HBNB_MYSQL_PWD'),
                                    getenv('HBNB_MYSQL_HOST'),
                                    getenv('HBNB_MYSQL_DB')),
                                    pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def remove(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def all(self, cls=None):
        cls_lst = ["Review", "City", "State", "User", "Place", "Amenity"]
        obj_lst = []
        if cls is None:
            for cls_type in cls_lst:
                obj_lst.extend(self.__session.query(cls_type).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            obj_lst = self.__session.query(cls).all()
        return {"{}.{}".format(type(obj).__name__, obj.id): obj for obj in obj_lst}

    def close(self):
        self.__session.close()

    def total(self):
        return len(self.__session.query(Review).all())
