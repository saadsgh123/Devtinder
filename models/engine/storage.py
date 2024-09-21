from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.testing.suite.test_reflection import users

from models.basemodel import Base
from models.User import User
from models.School import School
from models.Education import Education
from models.Technology import Technology

classes = {"School": School, "Education": Education, "Technology": Technology, "User": User}


class Storage:
    __engine = None
    __session = None

    def __init__(self):
        DB_USER = "root"
        DB_PASSWORD = "anasaad"
        DB_HOST = "localhost"
        DB_NAME = "test2"
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME))
        self.reload()

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)
        self.__session.commit()

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    # custom queries
    def get_user_by_email(self, email):
        objs = self.__session.query(User).filter(User.email == email).first()
        return objs

    def get_user_by_id(self, id):
        objs = self.__session.query(User).filter(User.id == id).first()
        return objs

    def get_user_by_username(self, username):
        objs = self.__session.query(User).filter(User.username == username).first()
        return objs

    def get_users_by_job_title(self, job_title):
        users = []
        objs = self.__session.query(User).filter(User.job_title.like(f"%{job_title}%"))
        for obj in objs:
            users.append(obj)
        return users

    def create_user_profile(self, username, email, password):
        new_user = User(username=username, email=email, password=password)
        new_user.save()
        return new_user

    def update_user_profile(self, id, country="", city="", firstname="", lastname="", job_title="", bio="",
                            small_bio="", location="", exp=1,  profile_pic="", github_url="",
                            facebook_url="", linkedln="", stackoverflow="", medium_url="", pro_mail=""):
        user = self.get_user_by_id(id)
        if user:
            user.job_title = job_title
            user.country = country
            user.city = city
            user.firstname = firstname
            user.lastname = lastname
            user.Exp = exp
            user.bio = bio
            user.small_bio = small_bio if small_bio else ""
            user.location = location
            user.profile_pic = profile_pic
            # to change attention
            # user.twitter_url = github_url
            user.github_url = github_url
            user.facebook_url = facebook_url
            user.linkedln = linkedln
            user.medium_url = medium_url
            user.pro_mail = pro_mail
            user.stackoverflow = stackoverflow

            self.__session.commit()

    def post_profile_pic(self, id, profile_pic):
        user = self.get_user_by_id(id)
        if user:
            user.profile_pic = profile_pic

            self.__session.commit()

