

if __name__ == '__main__':
    from models import storage
    from models.School import School
    from models.User import User
    from models.Technology import Technology

    print("=========== Create technologie =============")
    user = User(username="saadsgh123", email="saadsgh123@gmail.com", password="saad")
    tech1 = Technology(name="Python", picture="/static/images/python.png")
    user.technology.append(tech1)
    storage.session.add(user)
    storage.session.commit()
    storage.session.close()
    print("=========== END =============")
    print("")
