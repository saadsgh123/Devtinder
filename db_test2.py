# Import storage at the top (if circular dependency is fixed)
from models import storage

if __name__ == '__main__':
    # Delay import of user_tech_table to avoid potential circular dependency
    from models.relations import user_tech_table

    # Output for creating technologies
    print("=========== Create technologie =============")
    # Example of creating a user and technology (uncomment when ready)
    # user = User(username="saadsgh123", email="saadsgh123@gmail.com", password="saad")
    # tech1 = Technology(name="Python", picture="/static/images/python.png")
    # user.technology.append(tech1)
    # user.save()
    print("=========== END =============\n")

    # Output for adding a list of skills and assigning them to a user
    print("=========== Add a list of skills & assign them to a user =============")
    # Example for adding skills to a user (uncomment when ready)
    # skills = ["Python", "JavaScript", "HTML"]
    # user = User(id="", username="anasaad", email="anasaad@gmail.com", password="saad")
    # for skill in skills:
    #     tech = Technology(name=skill, picture="/static/images/python.png")
    #     user.technology.append(tech)
    # user.save()
    print("=========== END =============\n")

    # Output for getting user skills from the user_tech_table
    print("=========== Get user skills =============")
    tech_user = storage.all(user_tech_table).values()
    for v in tech_user:
        print(v)
    print("=========== END =============\n")
