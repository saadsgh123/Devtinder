from models.User import User
from models.Technology import Technology

if __name__ == '__main__':
    print("=========== Create technologie =============")
    # user = User(username="saadsgh123", email="saadsgh123@gmail.com", password="saad")
    # tech1 = Technology(name="Python", picture="/static/images/python.png")
    # user.technology.append(tech1)
    # user.save()
    print("=========== END =============")
    print("")

    print("=========== add a list of skills & assign them a user =============")
    skills = ["Python", "JavaScript", "HTML"]
    user = User(username="anasaad", email="anasaad@gmail.com", password="saad")
    for skill in skills:
        tech = Technology(name=skill, picture="/static/images/python.png")
        user.technology.append(tech)
    user.save()
    print("=========== END =============")
    print("")





