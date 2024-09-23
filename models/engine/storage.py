from flask import session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.basemodel import Base
from models.User import User
from models.School import School
from models.Education import Education
from models.Technology import Technology
from models.relations import user_tech_table

classes = {"School": School, "Education": Education, "Technology": Technology, "User": User,
           "UserTech": user_tech_table}


class Storage:
    __engine = None
    __session = None

    def __init__(self):
        DB_USER = "root"
        DB_PASSWORD = "anasaad"
        DB_HOST = "localhost"
        DB_NAME = "test5"
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

    @staticmethod
    def create_user_profile(username, email, password):
        new_user = User(username=username, email=email, password=password)
        new_user.save()
        return new_user

    def update_user_profile(self, id, country="", city="", firstname="", lastname="", job_title="", bio="",
                            small_bio="", location="", exp=1, github_url="",
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

    def get_all_tech(self):
        """ function that return a list of technologies
            Return: List<Technology>
         """
        techs = []
        objs = self.all(classes["Technology"]).values()
        for obj in objs:
            techs.append(obj)
        return techs

    def get_tech_by_name(self, name):
        return self.__session.query(Technology).filter(Technology.name == name).first()

    def get_technology_by_id(self, id):
        """Get a technology by its ID"""
        return self.__session.query(Technology).filter(Technology.id == id).first()

    def create_technology(self, name, picture):
        """Create a new technology"""
        new_technology = Technology(name=name, picture=picture)
        self.new(new_technology)
        return new_technology

    def update_technology(self, id, name=None, picture=None):
        """Update an existing technology"""
        tech = self.get_technology_by_id(id)
        if tech:
            if name:
                tech.name = name
            if picture:
                tech.picture = picture
            self.__session.commit()

    def delete_technology(self, id):
        """Delete a technology by ID"""
        tech = self.get_technology_by_id(id)
        if tech:
            self.delete(tech)
            self.save()

    def get_education_by_id(self, id):
        """Get an education record by its ID"""
        return self.__session.query(Education).filter(Education.id == id).first()

    def get_educations_by_user_id(self, user_id):
        """Get all education records for a specific user"""
        return self.__session.query(Education).filter(Education.user_id == user_id).all()

    def create_education(self, user_id, school_id, start_date, end_date):
        """Create a new education record"""
        new_education = Education(user_id=user_id, school_id=school_id, start_date=start_date, end_date=end_date)
        self.new(new_education)
        return new_education

    def update_education(self, id, school_id=None, start_date=None, end_date=None):
        """Update an existing education record"""
        education = self.get_education_by_id(id)
        if education:
            if school_id:
                education.school_id = school_id
            if start_date:
                education.start_date = start_date
            if end_date:
                education.end_date = end_date
            self.__session.commit()

    def delete_education(self, id):
        """Delete an education record by ID"""
        education = self.get_education_by_id(id)
        if education:
            self.delete(education)
            self.save()

    def get_school_by_id(self, id):
        """Get a school by its ID"""
        return self.__session.query(School).filter(School.id == id).first()

    def get_school_by_name(self, name):
        """Get a school by its name"""
        return self.__session.query(School).filter(School.name == name).first()

    def create_school(self, name):
        """Create a new school"""
        new_school = School(name=name)
        self.new(new_school)
        return new_school

    def update_school(self, id, name=None):
        """Update an existing school"""
        school = self.get_school_by_id(id)
        if school and name:
            school.name = name
            self.__session.commit()

    def delete_school(self, id):
        """Delete a school by ID"""
        school = self.get_school_by_id(id)
        if school:
            self.delete(school)
            self.save()
