from models import storage
from models.User import User
from models.Technology import Technology
from models.relations import user_tech_table

if __name__ == '__main__':
    print("=========== Create technologie =============")
    # user = User(username="saadsgh123", email="saadsgh123@gmail.com", password="saad")
    # tech1 = Technology(name="Python", picture="/static/images/python.png")
    # user.technology.append(tech1)
    # user.save()
    print("=========== END =============")
    print("")

    print("=========== add a list of skills & assign them a user =============")
    # skills = ["Python", "JavaScript", "HTML"]
    # user = User(id="", username="anasaad", email="anasaad@gmail.com", password="saad")
    # for skill in skills:
    #     tech = Technology(name=skill, picture="/static/images/python.png")
    #     user.technology.append(tech)
    # user.save()
    print("=========== END =============")
    print("")

    print("=========== get user skills =============")
    tech_user = storage.all(user_tech_table).values()
    for v in tech_user:
        print(v)
    print("=========== END =============")
    print("")





